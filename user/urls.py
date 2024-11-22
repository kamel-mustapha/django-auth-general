from django.urls import path
from user.views import register, login, me, activate, reset_password, reset_password_email

urlpatterns = [
    path('register', register),
    path('login', login),
    path('me', me),
    path('activate', activate),
    path('reset-password-init', reset_password_email),
    path('reset-password', reset_password)
]
