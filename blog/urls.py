from django.urls import path, include
from blog import views


urlpatterns = [
    path('', views.Home_as_view, name='home'),
]