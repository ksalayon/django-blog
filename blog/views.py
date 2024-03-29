from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View

from .models import Post, Page, Navigation, Comment, Category

# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    navigation_list = Navigation.objects.order_by('order')
    context = {'latest_post_list': latest_post_list, 'navigation_list': navigation_list}
    return render(request, 'blog/index.html', context)

class PostView(View):
    template_name = 'blog/post.html'
    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs['pk'])
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        latest_comments = Comment.objects.filter(post=post, approved=True).order_by('-created')[:10]
        return render(request, self.template_name, {'post': post, 'latest_comments': latest_comments})

class PageView(generic.DetailView):
    #response = "You're looking at the page with id %s."
    #return HttpResponse(response % page_id)
    model = Page
    template_name = 'blog/page.html'

class CategoryPostsView(View):
    template_name = 'blog/category_posts.html'

    def get(self, request, *args, **kwargs):
        category = Category.objects.get(pk=self.kwargs['pk'])
        category_posts = Post.objects.filter(categories=category).order_by('pub_date')[:5]
        return render(request, self.template_name, {'category_posts': category_posts, 'category': category})

    

def comment_on_post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    commenter_website = request.POST['website']
    ip_address = get_client_ip(request)
    
    try:
        commenter_name = request.POST['name']
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/post.html', {
            'post': p,
            'error_message': "You didn't enter a name.",
        })
    try:
        commenter_email = request.POST['email']
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/post.html', {
            'post': p,
            'error_message': "You didn't enter an email.",
        })
    try:
        comment = request.POST['comment']
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'blog/post.html', {
            'post': p,
            'error_message': "You didn't enter a comment.",
        })
    else:
        c = Comment(post=p, commenter_name = commenter_name, commenter_email = commenter_email, commenter_website = commenter_website, comment = comment, ip_address = ip_address)
        c.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blog:post', args=(p.id,)))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip