from django.shortcuts import render, redirect
from .models import BlockPost
from .forms import NewPost, EditPost
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    """Home page with each of messages of user`s blog"""
    posts = BlockPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """Add a new post on blog of user"""
    if request.method != 'POST':
        # datas is not sent; create an empty form
        form = NewPost()
    else:
        # datas 'POST' was sent; processing he datas
        form = NewPost(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit a separate post"""
    post = BlockPost.objects.all()
    # post = BlockPost.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # source request; form is fills in with the data of current post
        form = EditPost(instance=post)
    else:
        # datas 'POST' was sent; processing the data
        form = EditPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)

