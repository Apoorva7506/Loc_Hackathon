from django.shortcuts import render, redirect, get_object_or_404
from . models import News, Comment
# Create your views here.
import requests
from bs4 import BeautifulSoup
import re
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings

'''def news_make(request):

	url = 'https://www.indiatoday.in/crime'

	#titlelist=[]
	#desclist=[]
	piclist=[]
	mainlist=[]

	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	for a in soup.find_all('div', class_='catagory-listing'):
		picdet=a.find('div',attrs={'class': 'pic'})
		pic=a.find('img', {'src':re.compile('.jpeg')})
		det=a.find('div',attrs={'class': 'detail'})
		main=det.find('a',href=True)
		desc=det.find('p')
		titlelist.append(main.text)
		desclist.append(desc.text)
		piclist.append(pic)
		mainlist.append(main)
		if pic['src']!=None:
			news=News.objects.create(title=main.text,description=desc.text,img=pic['src'])
		else:
			news=News.objetcs.create(title=main.text,description=desc.text)
	for i in range(len(piclist)-2):
		news=News.objects.create(title=titlelist[i],description=desclist[i],img=piclist[i]['src'])
	for i in range(len(piclist)-2+1,len(piclist)):
		news=News.objects.create(title=titlelist[i],description=desclist[i])
	
	return HttpResponse("It Works")'''

def news_list(request):
	news=News.objects.all()

	return render(request,'news/news_list.html',{'news':news})

def news_detail(request,nk):
	news=get_object_or_404(News, pk=nk)	
	com=Comment.objects.filter(news=news).order_by('-created_date')
	return render(request,'news/news_detail.html',{'news':news,'com':com})

def add_comment(request,nk):
	#import pdb; pdb.set_trace()
	new_comment=Comment.objects.create(comment=request.POST.get('comment', False),user=request.user,created_date=datetime.now(), news=get_object_or_404(News, pk=nk)	 )
	#new_comment.username=request.user
	#new_comment.news=get_object_or_404(News, pk=nk)	
	#new_comment.created_date=datetime.now
	#new_comment.save()
	return redirect('news_detail', nk=nk)

#def add_comment44(request, nk):
#    news = get_object_or_404(Post, pk=nk)
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.news = news
#            comment.save()
#            return redirect('news_detail', pk=post.pk)
#    else:
#        form = CommentForm()
#    return render(request, 'news/news_details.html', {'form': form})
