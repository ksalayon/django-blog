from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.html import strip_tags
import logging
from django.utils import timezone

logger = logging.getLogger('Model Logger')

# Create your models here.
class Navigation(models.Model):
    label = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    
    EXTERNAL_ANCHOR = 'external'
    PAGE_ANCHOR = 'page'
    POST_ANCHOR = 'post'
    TYPE_CHOICES = (
        (EXTERNAL_ANCHOR, 'External'),
        (PAGE_ANCHOR, 'Page'),
        (POST_ANCHOR, 'Post'),
    )
    type = models.CharField(default=EXTERNAL_ANCHOR, choices=TYPE_CHOICES, max_length = 8)

    TARGET_SELF = '_self'
    TARGET_BLANK = '_blank'
    TARGET_CHOICES = (
        (TARGET_SELF, 'Self'),
        (TARGET_BLANK, 'Blank')
    )
    target = models.CharField(default=TARGET_SELF, choices=TARGET_CHOICES, max_length = 7)
    url = models.URLField(blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    #Generic FK
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    
    subnavigations = models.ManyToManyField("self", symmetrical=False, blank=True, null=True)
    
    def href(self):
        if self.type == self.PAGE_ANCHOR:
            return '/blog/page/' + str(self.object_id)
        elif self.type == self.POST_ANCHOR:
            return '/blog/post/' + str(self.object_id)
        else:
            return self.url
        
    def get_subnavigations(self):
        return self.subnavigations.order_by('label')     
        
    def __str__(self):              # __unicode__ on Python 2
        return self.label
    class Meta:
        ordering = ('order',)

class Page(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    content = models.TextField();
    created = models.DateTimeField('date created', default = timezone.now())
    modified = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    
    def excerpt(self):
        maxWidth = 6
        words = strip_tags(self.content).split()
        return ' '.join(words[0:maxWidth]) + '...'
    
    excerpt.admin_order_field = 'content'

class Category(models.Model):
    label = models.CharField(max_length=100)
    
    #Generic FK
    sub_categories = models.ManyToManyField("self", symmetrical=False, blank=True, null=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.label
    class Meta:
        ordering = ('label',)

class Tag(models.Model):
    label = models.CharField(max_length=100)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.label
    class Meta:
        ordering = ('label',)

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    feature_image = models.ImageField(upload_to='post', null=True)
    content = models.TextField();
    allow_comment = models.BooleanField(default=True)
    created = models.DateTimeField('date created', default = timezone.now())
    modified = models.DateTimeField(blank=True, null=True)
    
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    class Meta:
        ordering = ('pub_date',)
        
    def excerpt(self):
        maxWidth = 6
        words = strip_tags(self.content).split()
        
        return ' '.join(words[0:maxWidth]) + '...'
    excerpt.admin_order_field = 'content'
        
class Comment(models.Model):
    
    #Creates one to many relationship
    post = models.ForeignKey(Post)
    
    commenter_name = models.CharField(max_length=100)
    commenter_email = models.EmailField()
    commenter_website = models.URLField(blank=True, null=True)
    comment = models.TextField();
    ip_address = models.GenericIPAddressField();
    created = models.DateTimeField('date created', default = timezone.now())

    def __str__(self):              # __unicode__ on Python 2
        #return self.label
        return self.excerpt()#self.wrap(self.comment, 100)
    
    def excerpt(self):
        maxWidth = 6
        words = strip_tags(self.comment).split()
        
        return ' '.join(words[0:maxWidth]) + '...'
    excerpt.admin_order_field = 'comment'
    
    