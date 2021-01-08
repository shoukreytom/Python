from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.utils.feedgenerator import Atom1Feed

from .models import Post


class PostFeed(Feed):
    feed_type = Atom1Feed
    title = "My Blog"
    link = ""
    description = "New Posts of My Blog"

    def items(self):
        return Post.objects.filter(status='published')
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords(item.content, 30)