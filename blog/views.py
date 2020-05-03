from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blogpic(request):
    blogs=Blog.objects
    return render(request,'blog/bloghome.html',{'blogs':blogs})

def blog_detail(request,blog_id):
    detailblogs=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/blogdetail.html',{'blogdetail':detailblogs})
