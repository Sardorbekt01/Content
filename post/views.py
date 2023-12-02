from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Profile

def post(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.image)
    return render(request, 'post.html', {'posts':posts})

def detail(request, pk):
    post = Post.objects.get(id=int(pk))
    return render(request, 'content.html', {'post':post})

def profile(request):
    profiles = Profile.objects.all()
    for profile in profiles:
        print(profile.image)
    return render(request,'post.html',)