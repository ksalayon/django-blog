from django.contrib import admin
from .models import Navigation, Page, Category, Post, Comment, Tag

# Register your models here.

class NavigationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['label', 'type', 'order']}),
        ('Target', {'fields': ['target', 'url', 'content_type', 'object_id']}),
        (None, {'fields': ['sub_navigations']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('label', 'order', 'type', 'object_id')
 
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    list_filter = ['pub_date']

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'pub_date', 'excerpt')
    list_filter = ['pub_date']
    search_fields = ['title']
    
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'excerpt')
    list_filter = ['pub_date']
    search_fields = ['title']
    

admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)