from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap
}


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.post_detail, name='post-detail'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]