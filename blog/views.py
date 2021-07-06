from django.shortcuts import render

# Create your views here.
from .models import *


def Home_as_view(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    categories = Categories.objects.all()
    return render(request, 'blog/home.html', context={
        'feed':queryset,
        'categories': categories,
    })


def PostDetail_as_view(request, pk):
    post = Post.objects.get(id=pk)
    categories = Categories.objects.all()
    return render(request, 'blog/post_detail.html', context={
        'post' : post,
        'categories': categories,
    })

def About_as_view(request):
    categories = Categories.objects.all()
    return render(request, 'blog/about.html', context={
        'categories': categories,
    })

def Search(request):
    
	if request.method == 'GET':
		search = request.GET.get('search-text')
		titles = Post.objects.filter(title__contains = search)
		contents = Post.objects.filter(content__contains = search)

    


	context = {'titles':titles, 'contents':contents}
	return render(request, 'blog/search.html',context)
