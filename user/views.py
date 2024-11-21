from user.view_imports import *

def register(req):
    if req.method != "POST": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    body = json.loads(req.body)
    
    form = UserRegisterForm(data=body)
    
    if form.is_valid():
        form.save()
        
        return JsonResponse({}, status=201)
    else:
        errors = json.loads(form.errors.as_json())
        
        return JsonResponse(errors, status=400, safe=False)

def login(req):
    if req.method != "POST": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    body = json.loads(req.body)
   
    user = authenticate(username=body.get("username"), password=body.get("password"))
    
    if user is None: return JsonResponse({"message": "Please provide a valid username and password"}, status=400)
    
    exp_timestamp= get_time_delta(hours=24)
    
    encoded_refresh_token = {
        "id": user.id, 
        "username": user.username,
        "email": user.email,
        "iat": int(time.time()) ,
        "exp": exp_timestamp
    }

    refresh_token = jwt.encode(encoded_refresh_token, settings.SECRET_KEY, algorithm="HS256")
    
    res = HttpResponse("")
    
    res.set_cookie('refresh_token', refresh_token)
    
    return res

def me(req):
    if req.method != "GET": return JsonResponse({'message': 'METHOD_NOT_ALLOWED'}, status=400)
    
    refresh_token = req.COOKIES.get("refresh_token")
    
    if not refresh_token: return JsonResponse({'message': "INVALID_REFRESH_TOKEN"}, status=400)
    
    decoded_token = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=["HS256"])
    
    if not decoded_token.get("exp") or int(time.time()) > decoded_token.get("exp"):
        return JsonResponse({'message': "INVALID_REFRESH_TOKEN"}, status=400)
    
    user = User.objects.filter(id=decoded_token.get("id"))
    
    if not user:
        return JsonResponse({'message': "INVALID_REFRESH_TOKEN"}, status=400)
    
    user = user[0]
    
    exp_timestamp = get_time_delta()
    
    encoded_access_token = {
        "id": user.id, 
        "username": user.username,
        "email": user.email,
        "iat": int(time.time()) ,
        "exp": exp_timestamp
    }

    encoded_jwt = jwt.encode(encoded_access_token, settings.SECRET_KEY, algorithm="HS256")
    
    return JsonResponse({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "access_token": encoded_jwt
    })
