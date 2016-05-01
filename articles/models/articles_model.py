from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, null=False)
    author = models.CharField(max_length=128, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=False)
    primary_color = models.CharField(max_length=128, null=True, default='None')
    image = models.ImageField(upload_to='images',default='data.png')
    image_alt = models.CharField(max_length=128, default="image")
    published_date = models.DateTimeField(auto_now_add=True)
    last_saved = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    email = models.EmailField(primary_key=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_saved = models.DateTimeField(auto_now=True)

from django.contrib import admin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'

