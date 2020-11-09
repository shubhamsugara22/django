from django.shortcuts import render
from . models import Post, Comments
# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,

    }
    return render(request, "blog/blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    )
    context = {
        "posts": posts,
        "category": category,

    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comments.objects.filter(post=posts)
    context = {
        "posts": posts,
        "comments": comments,

    }
    return render(request, "blog/bolg_detail.html", context)
