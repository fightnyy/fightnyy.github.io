from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def create(request):
    return render(request,'posting/create.html')


def post(request):
    blogs=Blog.objects
    return render(request,'posting/post.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'posting/detail.html',{'blog_detail':blog_detail})

def new(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/posting/'+str(blog.id))


