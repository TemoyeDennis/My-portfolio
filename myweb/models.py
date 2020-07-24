from django.db import models

# Create your models here.
# Create your models here.
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime, date


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    prod_image = models.ImageField(default='default.jpeg', upload_to='statics/images/project_images')

    def get_absolute_url(self):
        return reversed('project_images')

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    serv_image = models.ImageField(default='default.jpeg', upload_to='statics/images/Services_images')

    def get_absolute_url(self):
        return reversed('Services_images')

    def __str__(self):
        return self.title


class Post(models.Model):
    UserId = models.CharField(max_length=20)
    PostId = models.CharField(max_length=20)
    PostTitle = models.CharField(max_length=100)
    PostTime = models.CharField(max_length=100)
    PostDate = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpeg', upload_to='statics/images/Post_images')

    def __str__(self):
        return self.PostTitle

    def get_absolute_url(self):
        return reversed('Post_images')


class Comment(models.Model):
    UserId = models.CharField(max_length=20)
    CommentId = models.CharField(max_length=20)
    CommentTitle = models.CharField(max_length=100)
    CommentTime = models.CharField(max_length=100)
    CommentDate = models.CharField(max_length=100)
    Comment = models.CharField(max_length=100)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.post


class Reply(models.Model):
    UserId = models.CharField(max_length=20)
    ReplyId = models.CharField(max_length=20)
    ReplyTitle = models.CharField(max_length=100)
    CommentId = models.CharField(max_length=100)
    ReplyDate = models.CharField(max_length=100)
    Reply = models.CharField(max_length=100)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.comment
