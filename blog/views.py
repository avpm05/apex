# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .form import CommnetForm
from django.shortcuts import render
from    django.shortcuts import render,reverse,get_object_or_404
from .models import BlogPosts,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def BlogPostsList(request):
    object_list = BlogPosts.published.all()
    my_paginator  = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = my_paginator.page(page)
    except PageNotAnInteger:
        posts = my_paginator.page(1)
    except EmptyPage:
        posts = my_paginator.page(my_paginator.num_pages)

    return render(request,'blog.html',{'posts':posts,'page':page})

def postdetail(request,year,month,day,slug_post):
          post = get_object_or_404(BlogPosts,slug = slug_post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
          comments = post.comments.filter(active=True)

          if request.method =='POST':
              comment_form = CommnetForm(data=request.POST)
              if comment_form.is_valid():
                  new_comment = comment_form.save(commit=False)
                  new_comment.post = post
                  new_comment.save()
          else:
              comment_form = CommnetForm()

          return render(request,'postdetail.html',{'post': post,'comments': comments,'comment_form': comment_form})