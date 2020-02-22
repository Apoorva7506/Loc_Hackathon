from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('fir/mo',views.fir_mo,name='mo'),
    path('register',views.register,name='register'),
    
]