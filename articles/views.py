from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle
from comments.forms import *

# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    comments = Comment.objects.filter(article=article)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.article=article
            comment.user=request.user
            comment.save()
            return redirect('articles:detail',slug=slug)
    else:
        form=CommentForm()
    return render(request,'articles/article_detail.html',{'article':article,'comments': comments,'form':form})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form = CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()
            #save article to DB
            return redirect('articles:list')
    else:
        form =CreateArticle()
    return render(request,'articles/article_create.html',{'form':form}) # see line no.9 in article_create.html


# def article_detail(request,slug):
#     article = Article.objects.get(slug=slug)
#     comment = Comment.objects.filter(article=article)
#     if request.method=='POST':
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             comment =form.save(commit=False)
#             comment.article=article
#             comment.user=request.user
#             comment.save()
#             return redirect('articles:detail',slug=slug)
#     else:
#         form=CommentForm()
#     return render(request,'articles/article_detail.html',{'article':article})
        # return HttpResponse(slug)

