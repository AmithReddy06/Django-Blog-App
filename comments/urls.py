from django.urls import path
from . import views

app_name='comments'

urlpatterns =[
    path('create/<int:article_id>/', views.comment_create, name='create'),
    path('delete/<int:comment_id>/', views.comment_delete, name='delete')
]