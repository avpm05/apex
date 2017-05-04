from django.contrib import admin
from search.models import Sources
from blog.models import BlogPosts

# Register your models here.
class SourceAdmin(admin.ModelAdmin):
    list_display = ('Name','Url','Type','Description')
admin.site.register(Sources,SourceAdmin)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title','publish' )
admin.site.register(BlogPosts,PostsAdmin)
