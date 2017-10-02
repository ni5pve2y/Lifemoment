from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_complete,
    password_reset_confirm,
)

from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^communication/', include('communication.urls', namespace='communication')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^$', views.startpage, name='startpage'),

    url(r'^password-reset/$', password_reset, {'template_name': 'accounts/password_reset.html'}, name='password_reset'),
    url(r'^password-reset/done/$', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', password_reset_complete, name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
