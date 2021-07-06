from django.shortcuts import render

# Create your views here.
from .models import *


def Home_as_view(request):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/home.html', context={
        'feed':queryset,
    })