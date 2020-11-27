from django.shortcuts import render
from . models import Post, Comments
from . forms import CommentForm
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
    ).order_by("-created_on")
    context = {
        "posts": posts,
        "category": category,

    }
    return render(request, "blog/blog_category.html", context)


def blog_detail(request, pk):
    posts = Post.objects.get(pk=pk)
    comments = Comments.objects.filter(posts=posts)
    form = CommentForm()

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comments(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                posts=posts,
            )
            comment.save()
    #comments = Comments.objects.filter(posts=posts)
    context = {
        "posts": posts,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/blog_detail.html", context)
