from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    return render(request, 'mse1/posts.html', {'posts':posts})

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'mse1/detail.html', {'post': post})
