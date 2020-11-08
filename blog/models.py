from django.db import models

# Create your models here.

# cateogry model with single parameter


class Category(models.Model):
    name = models.CharField(max_length=20)

# post parameter for posting blog with content ,title, created date ,modified date and categories


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='posts')

# comment section model


class Comments(models.Model):
    author = models.CharField(max_length=25)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey('Post', on_delete=models.CASCADE)
