from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('show/', views.show, name='show'),
    path('edit/',views.edit,name='edit'),
]