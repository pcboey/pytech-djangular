from django.conf.urls import patterns, url
from .views import PublisherList, PublisherDetail, PublisherBookList, PublisherCreate, PublisherUpdate

urlpatterns = patterns('',
    url(r'^publishers/$', PublisherList.as_view(), name='publisher-list'),
    url(r'^publisher/detail/(?P<pk>[0-9]+)/$', PublisherDetail.as_view(), name='publisher-detail'), 
    url(r'^publisher/add/$', PublisherCreate.as_view(), name='publisher-add'), 
    url(r'^publisher/([\w-]+)/$', PublisherBookList.as_view()),
    url(r'publisher/update/(?P<pk>[0-9]+)/$', PublisherUpdate.as_view(), name='publisher-update'),                   
)
