from django.shortcuts import render, get_object_or_404
from .models import Post,Comment,Category,pin


def show_category(request):

    category = Category.objects.all()
    return render(request, 'Category_list.html', {'category': category})


def post_list(request , category_id):
    posts = Post.objects.filter(status='published',Category=category_id)
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    comments = Comment.objects.filter(post=post)
    like_count = post.like_count()


    return render(request, 'post_detail.html', {'post': post , 'comments': comments , 'like_count': like_count})


def user_pins(request):
    posts_pins = pin.objects.filter(author=request.user).values_list('post_name', flat=True)
    posts = Post.objects.filter(status='published', id__in=posts_pins)
    return render(request, 'post_list.html', {'posts': posts})