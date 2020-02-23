from django.contrib import admin
from django.urls import path,include
from . views import news_list, news_detail, add_comment

urlpatterns = [
	#path('',news_make,name='news_make'),
	path('',news_list, name='news_list'),
	path('news_detail/<int:nk>',news_detail, name='news_detail'),
	path('add_comment/<int:nk>',add_comment, name='add_comment')
]
