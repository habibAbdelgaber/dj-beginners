from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    return render(request, 'home/home.html', {'posts': posts})


def create(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please login to add new post!')
        return redirect('home-page')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            form.author = request.user
            author.save()
        
        return redirect('home-page')
    form = PostForm()
    return render(request, 'home/create.html', {'form': form})

def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'home/detail.html', {'post': post})

def update(request, pk):
    if not request.user.is_authenticated:
        messages.info(request, 'please login to update your post')
        return redirect('home-page')
    
    post = Post.objects.get(id=pk)
    form = PostForm()
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        author = form.save(commit=False)
        form.author = request.user
        author.save()
        messages.success(request, 'You have updated the post successfully!')
        return redirect('post-detail', pk=post.id)
    form = PostForm(request.POST or None, instance=post)
    return render(request, 'home/update.html', {'form': form})
        

def delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    return render(request, 'home/delete.html', {'post': post})
