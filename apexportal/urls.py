"""apexportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
    url(r'^', include('audit.urls')),
    url(r'^', include('cve.urls')),
    url(r'^', include('news.urls')),
    url(r'^', include('intelligience.urls')),
    url(r'^', include('scan.urls')),
    url(r'^', include('search.urls')),
    url(r'^', include('blacklist.urls')),
    url(r'^', include('blog.urls',namespace='blog',app_name='blog')),
]
