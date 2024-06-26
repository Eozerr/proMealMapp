"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path,include
from app.views import index,calculate,register,login,custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  # new
    path('', index, name='index'),
    path('index', index, name='index'),
    path('calculate.html', calculate, name='calculate'),
    path('calculate', calculate, name='calculate'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),  # Giriş için URL deseni
    path('logout/', custom_logout, name='logout'),
]
