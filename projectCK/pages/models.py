from django.db import models
from django.db.models.fields import Field, related
from django.urls import reverse # new
from datetime import datetime, date

from django.utils.translation import activate

class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null= True, blank= True,upload_to="images/")
    author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
    )
    body = models.TextField()
    post_date= models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
def __str__(self):
    return self.title
    
def get_absolute_url(self): # new
    #return reverse('post_detail', args=[str(self.id)])
    return reverse('home')

class Comment (models.Model):
    post = models.ForeignKey(Post, related_name= "comment", on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    body= models.TextField()
    data_added = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)