import json, jwt, time, datetime
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm  
from user.forms import UserRegisterForm
from django.conf import settings
from user.models import User
from user.utils import get_time_delta