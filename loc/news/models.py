from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
# Create your models here.

class News(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	img = models.TextField(null=True, blank=True)

class Comment(models.Model):
	news = models.ForeignKey(News, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	comment = models.TextField()
	created_date = models.DateTimeField(default=datetime.now)