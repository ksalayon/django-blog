from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/post/5/
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    # ex: /blog/page/5/
    url(r'^page/(?P<page_id>[0-9]+)/$', views.page, name='page'),
    # ex: /blog/category/5/posts/
    url(r'^category/(?P<category_id>[0-9]+)/posts/$', views.category_posts, name='category_post'),
    # ex: /blog/post/5/comment
    url(r'^post/(?P<post_id>[0-9]+)/comment/$', views.comment_on_post, name='comment_on_post'),
]