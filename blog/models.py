from django.db import models
from django.urls import reverse # new
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    post_date= models.DateField(auto_now_add=True)
    likes =models.ManyToManyField('auth.User', related_name='blog_post')
def __str__(self):
    return self.title
    
def get_absolute_url(self): # new
    #return reverse('post_detail', args=[str(self.id)])
    return reverse('home')

