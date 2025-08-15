from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm

def post_list(request, slug=None):
    posts = Post.objects.filter(published=True)
    tag = None
    if slug:
        tag = get_object_or_404(Tag, slug=slug)
        posts = posts.filter(tags=tag)
    return render(request, 'blog/post_list.html', {'posts': posts, 'active_tag': tag})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    comments = post.comments.filter(approved=True)
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save(commit=True)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'is_edit': True})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_delete_confirm.html', {'post': post})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return redirect('post_detail', pk=post.pk)

def search(request):
    q = request.GET.get('q', '').strip()
    posts = Post.objects.filter(published=True)
    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(tags__name__icontains=q)).distinct()
    return render(request, 'blog/post_list.html', {'posts': posts, 'query': q})
