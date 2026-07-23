from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Count

def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments'))
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post':post})


    
    


