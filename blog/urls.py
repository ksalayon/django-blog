from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/post/5/
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    # ex: /blog/page/5/
    url(r'^page/(?P<pk>[0-9]+)/$', views.PageView.as_view(), name='page'),
    # ex: /blog/category/5/posts/
    url(r'^category/(?P<pk>[0-9]+)/posts/$', views.CategoryPostsView.as_view(), name='category_posts'),
    # ex: /blog/post/5/comment
    url(r'^post/(?P<post_id>[0-9]+)/comment/$', views.comment_on_post, name='comment_on_post'),
]