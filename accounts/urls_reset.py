from django.urls import re_path as url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$', PasswordResetView.as_view(),
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', password_reset_complete, name='password_reset_complete'),
]
