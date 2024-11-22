import json, datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm  
from user.forms import UserRegisterForm
from django.conf import settings
from user.models import User
from user.utils import *
from django.core.mail import send_mail
from user.html_templates import register_template, invalid_token, activation_success, account_already_activated, reset_password_link, reset_password_success
from django.views.decorators.csrf import csrf_exempt
