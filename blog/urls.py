from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Agreement_list, name='post_list'),
    url(r'^$', views.Request_list, name='post_list'),
    url(r'^Agreement/(?P<pk>\d+)/$', views.Agreement_detail, name='Agreement_detail'),
    url(r'^Request/(?P<pk>\d+)/$', views.Request_detail, name='Request_detail'),
    url(r'^Request/$', views.Request_list),
    url(r'^Agreement/$', views.Agreement_list),
    url(r'^RegRequest/$', views.RegRequest_list),
    url(r'^RegAgreement/$', views.RegAgreement_list),
    url(r'^Agreement/new/$', views.Agreement_new, name='Agreement_new'),
    url(r'^Agreement/(?P<pk>\d+)/edit/$', views.Agreement_edit, name='Agreement_edit'),
    url(r'^Request/new/$', views.Request_new, name='Request_new'),
    url(r'^Request/(?P<pk>\d+)/edit/$', views.Request_edit, name='Request_edit'),
    url(r'^search/$', views.search, name='search'),
    url(r'^search_form/$', views.search_form, name='search_form'),
]
