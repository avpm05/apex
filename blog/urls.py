from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/', views.BlogPostsList,name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<slug_post>[-\w]+)/$',views.postdetail,name='postdetail'),
    ]