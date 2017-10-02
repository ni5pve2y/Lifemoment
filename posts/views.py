from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import CreateCommentForm, CreatePostForm
from posts.models import Post, Comment


def post_list(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('posts:post_list')
    else:
        post_create_form = CreatePostForm()
        context = {
            'post_create_form': post_create_form,
        }
        return render(request, 'posts/post_create.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect('posts:post_detail', slug=slug)
    else:
        context = {
            'post': post,
            'comments': Comment.objects.filter(post=post),
            'form': CreateCommentForm(),
        }
        return render(request, 'posts/post_detail.html', context)


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, user=request.user)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts:post_detail', slug=slug)
    else:
        form = CreatePostForm(instance=post)
        context = {
            'form': form,
        }
        return render(request, 'posts/post_edit.html', context)


def post_delete(request, slug):
    # only user himself can delete post
    get_object_or_404(Post, slug=slug, user=request.user).delete()
    return render(request, 'posts/post_delete.html', {})
