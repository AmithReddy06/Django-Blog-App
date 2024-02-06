from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from comments.models import Comment

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='defgal.webp',blank=True)
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE) # whenever u add a new field, do makemigrations and migrate 
    comments = models.ManyToManyField(Comment, related_name='article_comments')


# class Comment(models.Model):
#     text = models.TextField()
#     author =  models.ForeignKey(User, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
#     created_date = models.DateTimeField(default=timezone.now)

    # add thumbnail and author later 


    def __str__(self):
        return self.title   
    
    def snippet(self):
        return self.body[:50]+ '...'
    

