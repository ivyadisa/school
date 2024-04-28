from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def upload_blogs(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        picture = request.POST.get('image')

        blogs, created = Blogs.objects.get_or_create(title=title, content=content, picture=picture)

        return redirect('blogs')
    
    return render(request, 'uploads.html')

def list_blogs(request):
    blogs = Blogs.objects.all().order_by('-uploaded_on')
    return render(request, 'blogs.html', {'blogs':blogs})

def detail_blogs(request, blog_id):
    blog_post = get_object_or_404(Blogs, id=blog_id)

    comment_list = Comments.objects.filter(blog_post=blog_post).order_by('-commented_on')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_post = blog_post
            comment.save()
            return redirect('blog-detail', blog_id)
    else:
        comment_form = CommentForm()
        
    return render(request, "blog-details.html", {"blog_post": blog_post, 'comment_form':comment_form, 'comment_list':comment_list})

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form" : form})