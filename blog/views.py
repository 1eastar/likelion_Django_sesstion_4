from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.content = request.GET['content']
    blog.save()
    return redirect('/blog/'+str(blog.id))
