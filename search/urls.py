from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.apexsearch),
    url(r'^search/company', views.company_list),

    ]