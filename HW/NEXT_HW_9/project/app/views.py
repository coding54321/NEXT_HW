from django.shortcuts import render, redirect
from datetime import date
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('date')
    today = date.today()
    for post in posts:
        if post.date:  
            delta = post.date - today
            post.d_day = delta.days
        else:
            post.d_day = 'N/A'  
    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST' :
        post_date = request.POST.get('date', date.today())
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date = post_date
        )
        return redirect('detail', new_post.pk)
    
    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    today = date.today()
    if post.date: 
        delta = post.date - today
        post.d_day = delta.days
    else:
        post.d_day = 'N/A'  
    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    
    if request.method == 'POST' :
        post_date = request.POST.get('date', post.date)
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date = post_date
        )

        return redirect('detail', post.pk)
    
    return render(request, 'update.html', {'post':post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('home')