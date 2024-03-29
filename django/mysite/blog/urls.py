"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.home),
    path(r'1', views.home2),
    re_path(r'register',views.register,name='reg'),
    re_path(r'homepage', views.homepage, name='home'),
    re_path(r'test', views.test, name='test'),
    re_path(r'login', views.login, name='login'),
    re_path(r'suc', views.suc, name='suc'),
    re_path(r'stu', views.stu, name='student'),
]
