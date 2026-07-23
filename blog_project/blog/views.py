from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.db.models import Count
from blog.forms import CommentForm

def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments'))
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', id=post.id)
        
    else:
        form = CommentForm()
            
    
    return render(request, 'blog/post_detail.html', {'post':post, 'form':form})


    
    


