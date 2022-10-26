from django.contrib import admin
from .models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=("js/tinyinject.js",)
        
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)