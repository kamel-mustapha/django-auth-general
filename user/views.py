from user.view_imports import *

@csrf_exempt
def register(req):
    if req.method != "POST": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    body = json.loads(req.body)
    
    form = UserRegisterForm(data=body)
    
    if form.is_valid():
        user = form.save()
        
        try:
            activation_token = generate_jwt_token(user)
            registration_template = register_template(
                user.username, 
                settings.ACTIVATION_REDIRECT_URL + f"?token={activation_token}", 
                "1 hour", settings.SUPPORT_EMAIL)
            send_mail( 
                'Thank you for registering to our site', 
                "", 
                settings.EMAIL_HOST_USER, 
                [user.email,], 
                html_message=registration_template
            )
        except Exception as e:
            print(e)
        
        return JsonResponse({}, status=201)
    else:
        errors = json.loads(form.errors.as_json())
        
        return JsonResponse(errors, status=400, safe=False)


def activate(req):
    if req.method != "GET": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)

    token = req.GET.get("token")
    
    if not token: return HttpResponse(invalid_token)
    
    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    
    if int(time.time()) > decoded_token.get("exp"): return HttpResponse(invalid_token)
    
    user = User.objects.filter(id=decoded_token.get("id"))
    user = user[0]
    if(user.is_active): return HttpResponse(account_already_activated())
    
    user.is_active = True
    user.save()
    
    return HttpResponse(activation_success())


@csrf_exempt
def login(req):
    if req.method != "POST": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    body = json.loads(req.body)
   
    user = authenticate(username=body.get("username"), password=body.get("password"))
    
    if user is None: return JsonResponse({"message": "Please provide valid credentials or activate your account"}, status=400)
    
    user.last_login = datetime.datetime.now()

    user.save()

    refresh_token = generate_jwt_token(user, hours=0, days=180)
    
    res = HttpResponse("")
    
    res.set_cookie('refresh_token', refresh_token)
    
    return res


def me(req):
    if req.method != "GET": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    refresh_token = req.COOKIES.get("refresh_token")
    
    if not refresh_token: return JsonResponse({'message': "Please provide a refresh token"}, status=400)
    
    decoded_token = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
    
    if int(time.time()) > decoded_token.get("exp"):
        return JsonResponse({'message': "Your token is expired"}, status=400)
    
    user = User.objects.filter(id=decoded_token.get("id"))
    
    if not user or (user and not user[0].is_active):
        return JsonResponse({'message': "Your refresh token is expired or your account is inactive"}, status=400)
    
    user = user[0]
    
    access_token = generate_jwt_token(user)
    
    return JsonResponse({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "access_token": access_token
    })


def reset_password_email(req):
    if req.method != "GET": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)

    email = req.GET.get("email")

    if not email: return JsonResponse({'message': 'Please provide a valid email in your query params'}, status=400)

    user = User.objects.filter(email=email)

    if not user:  return JsonResponse({'message': 'No user with this email found'}, status=400)

    user = user [0]

    try:
        token = generate_jwt_token(user)
        send_mail( 
            'Reset your password', 
            "", 
            settings.EMAIL_HOST_USER, 
            [user.email,], 
            html_message=reset_password_link(
                settings.RESET_PASSWORD_LINK + f"?token={token}"
            )
        )
    except Exception as e:
        print(e)

    return HttpResponse("")


def reset_password(req):
    if req.method == "GET":
        token = req.GET.get("token")
        
        if not token: return HttpResponse("No token provided")

        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        
        if int(time.time()) > decoded_token.get("exp"): return HttpResponse(invalid_token)

        return render(req, "reset-password.html", {"id": decoded_token.get("id")})
    
    elif req.method == "POST":
        body = req.POST

        user = User.objects.filter(id=int(body.get("id")))
        if not user:  return HttpResponse('No user found')
        
        user = user[0]
        user.set_password(body.get("password"))
        user.save()
        
        return HttpResponse(reset_password_success())