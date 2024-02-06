from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment
from articles.models import Article
from django.contrib import messages


# @login_required
# def add_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.author =request.user
#             comment.save()
#             return redirect('article_detail',pk=comment.article.pk)
        
#     else:
#         form=CommentForm()
#     return render(request,'comments/add_comment.html',{'form':form})


@login_required(login_url="/accounts/login/")
def comment_create(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment was posted successfully!')
            return redirect('articles:detail', slug=article.slug)
    else:
        form = CommentForm()

    return render(request, 'comments/comment_create.html', {'form': form, 'article': article})

@login_required(login_url="/accounts/login/")
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        article_slug = comment.article.slug
        comment.delete()
        messages.success(request, 'Your comment was deleted successfully!')
        return redirect('articles:detail', slug=article_slug)
    else:
        messages.error(request, 'You do not have permission to delete this comment.')
        return redirect('articles:detail', slug=comment.article.slug)