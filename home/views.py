from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home/home.html', {'posts': posts})


def create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('home-page')
    form = PostForm
    return render(request, 'home/create.html', {'form': form})

def detail(request):
    pass


def update(request):
    pass


def delete(request):
    pass
