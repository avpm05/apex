from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^search/$', views.apexsearch),
    #url(r'^search/companies', views.company_list),
    url(r'^search/companies', views.CompaniesListView.as_view(),name='companies_list'),

    ]