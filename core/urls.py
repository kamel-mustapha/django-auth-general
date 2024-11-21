from django.contrib import admin
from django.urls import path, include

API_URL = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_URL}auth/', include('user.urls'))
]
