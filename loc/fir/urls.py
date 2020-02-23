from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('firmo',views.fir_mo,name='firmo'),
    path('firdp',views.fir_dp,name='firdp'),
    path('firmp',views.fir_mp,name='firmp'),
    path('firass',views.fir_ass,name='firass'),
    path("logout", views.logout, name='logout'),

    
]