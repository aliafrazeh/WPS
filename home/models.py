from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class ArticleWeb(models.Model):
	title = models.CharField(max_length=550,verbose_name="Title")
	slug = models.SlugField(max_length=25,verbose_name="Name Url Web",unique=True)
	description = models.TextField(max_length=2000)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	publish =models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=False)
	image = models.ImageField(upload_to="CSR-Image/",null=True,blank=True)
	def __str__(self):
		return "Title: "+self.title + " " + "url: "+self.slug