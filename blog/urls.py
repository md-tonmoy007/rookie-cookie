from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    path('', views.Home_as_view, name='home'),
    path('post-detail/<int:pk>/', views.PostDetail_as_view,name='post-detail'),
    path('about/', views.About_as_view, name='about'),
    path('search-result/', views.Search, name='search')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)