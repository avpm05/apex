# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from statistics import mode
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
from postgresql.driver.dbapi20 import dbapi_type
class PublishedManager(models.Manager):
        def get_queryset(self):
            return super(PublishedManager,self).get_queryset().filter(status='published')


class BlogPosts (models.Model):
    def get_absolute_url(self):
        return reverse('blog:postdetail',args=[self.publish.year, self.publish.strftime('%m'), self.publish.strftime('%d'), self.slug])
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    objects = models.Manager()
    published = PublishedManager()
    title = models.CharField(max_length = 250)
    body =  models.TextField()
    slug = models.SlugField(max_length = 250,unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    class Meta:
        db_table = 'BlogPosts'
        ordering = ('-publish',)

    def __str__(self):
        return self.title


