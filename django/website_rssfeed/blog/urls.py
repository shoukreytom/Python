from django.urls import path
from . import views
from .feeds import PostFeed


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
    path('rss/feed/', PostFeed(), name='rss-feed'),
]