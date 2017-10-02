from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add/$', views.post_create, name='post_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^edit/(?P<slug>[-\w]+)/$', views.post_edit, name='post_edit'),
    url(r'^remove/(?P<slug>[-\w]+)/$', views.post_delete, name='post_delete'),
]
