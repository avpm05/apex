# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from    django.shortcuts import render,reverse,get_object_or_404
from .models import BlogPosts

# Create your views here.
def BlogPostsList(request):
    posts = BlogPosts.published.all()
    return render(request,'blog.html',{'posts':posts})

def postdetail(request,year,month,day,slug_post):
    post = get_object_or_404(BlogPosts,slug = slug_post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,'postdetail.html',{'post':post})