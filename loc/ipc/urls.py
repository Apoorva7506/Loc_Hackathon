from django.contrib import admin
from django.urls import path,include
from . views import ipc

urlpatterns = [
	#path('',news_make,name='news_make')
	path('',ipc, name='ipc')
]
