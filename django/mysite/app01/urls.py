from django.urls import path

from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('show/', views.show, name='show'),
    path('login/', views.login, name='login'),
]