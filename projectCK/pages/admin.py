from django.contrib import admin
from django.db.models.fields import Field
from .models import Post, Comment
from django import forms


admin.site.register(Post)
admin.site.register(Comment)


