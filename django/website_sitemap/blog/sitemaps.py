from django.contrib import sitemaps
from .models import Post


class PostSitemap(sitemaps.Sitemap):
    changefreq = "weakly"
    priority = 0.8

    def items(self):
        return Post.objects.filter(status='published')
    
    def lastmod(self, obj):
        return obj.updated