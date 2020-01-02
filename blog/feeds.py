from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostsFeed(Feed):
    title = 'Scandinavia'
    link = '/blog/'
    description = 'Новые посты моего блога'

    def items(self):
        return Post.objects.all().filter(status='published')

    def item_title(self, item):
        return self.item_title

    def item_description(self, item):
        return truncatewords(item.body, 30)
