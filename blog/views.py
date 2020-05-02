from django.shortcuts import render
from .models import Blog
# Create your views here.
def blogpic(request):
    blogs=Blog.objects
    return render(request,'blog/bloghome.html',{'blogs':blogs})
