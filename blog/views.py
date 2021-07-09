from django.shortcuts import render

# Create your views here.
from .forms import *
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
    comments = post.comments.filter(active=True)
    new_comment = None
    categories = Categories.objects.all()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', context={
        'post' : post,
        'categories': categories,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
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
