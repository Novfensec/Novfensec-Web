from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Post

class StaticViewSitemap(Sitemap):

    priority=1.0

    def items(self):
        return ['home','about','blog','portfolio','contact']
        
    def location(self,item):
        return reverse(item)
        
class BlogViewSitemap(Sitemap):

    priority=0.7

    def items(self):
        return Post.objects.all()
        
    def lastmod(self, obj):
        return obj.timeStamp