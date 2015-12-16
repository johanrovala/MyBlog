from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category

# Create your views here.

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

