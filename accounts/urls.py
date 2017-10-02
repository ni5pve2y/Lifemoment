from django.conf.urls import url
from django.contrib.auth.views import login, logout

from accounts import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/startpage.html'}, name='logout'),
    url(r'^registration/$', views.register, name='register'),

    url(r'^(?P<current_user>[-?\w]+)/profile/$', views.profile, name='profile'),
    url(r'^(?P<current_user>[-?\w]+)/change-password/$', views.change_password, name='change_password'),
    url(r'^(?P<current_user>[-?\w]+)/change-image/$', views.change_image, name='change_image'),
    url(r'^(?P<current_user>[-?\w]+)/settings/$', views.settings, name='settings'),
    url(r'^(?P<current_user>[-?\w]+)/information/$', views.information, name='information'),

    url(r'^(?P<current_user>[-?\w]+)/friends/$', views.friends, name='friends'),
    url(r'^(?P<current_user>[-?\w]+)/friends/add/(?P<new_friend>[-?\w]+)/$', views.add_friend, name='add_friend'),
]
