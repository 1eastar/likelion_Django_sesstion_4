from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blog_all = Blog.objects.all()
    paginator = Paginator(blog_all, 3)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})

def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('/blog/'+str(post.id))
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form': form})