from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """Извлечение всех постов c статусом PUBLISHED"""
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    """Предоставление детальной информации о посте"""
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
