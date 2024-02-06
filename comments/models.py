from django.db import models
from django.utils import timezone
# from articles.models import Article 
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.TextField()
    author =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_authored')
    article=models.ForeignKey('articles.Article', on_delete=models.CASCADE,related_name='article_comments') # Using a string reference to the Article Model
    created_date= models.DateTimeField(default=timezone.now)
        