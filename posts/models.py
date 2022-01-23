from django.contrib import admin
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.TextField()
    img_name_big = models.CharField(max_length=200)
    img_name_small = models.CharField(max_length=200)
    upload_date = models.DateField(default=timezone.now)
    video_name = models.CharField(max_length=200, blank=True, default="")
    info = models.TextField(blank=True, default="")
    block_dropper = models.BooleanField(default=False)
    #description = models.TextField()

    def __str__(self):
        return f"Post object with title {self.title}"


class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"Idea: {self.title}"

admin.site.register(Post)
admin.site.register(Idea)
# Create your models here.
