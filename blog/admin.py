from django.contrib import admin
from .models import Navigation, Page, Category, Post, Comment

# Register your models here.

class NavigationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['label', 'type']}),
        ('Target', {'fields': ['anchor', 'url', 'content_type', 'object_id']}),
        (None, {'fields': ['sub_navigations']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('label', 'type', 'object_id')
 
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1
    list_filter = ['pub_date']
    list_filter = ['created']

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ('title', 'pub_date', 'excerpt')
    list_filter = ['pub_date']
       
admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Page)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)