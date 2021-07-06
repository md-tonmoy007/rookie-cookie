from os import name
from django.urls import path, include
from blog import views


urlpatterns = [
    path('', views.Home_as_view, name='home'),
    path('post-detail/<slug:pk>/', views.PostDetail_as_view,name='post_detail'),
    path('about/', views.About_as_view, name='about'),
    path('search-result/', views.Search, name='search')
]