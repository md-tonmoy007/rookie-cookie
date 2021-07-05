from django.shortcuts import render

# Create your views here.
def Home_as_view(request):
    return render(request, 'blog/home.html')