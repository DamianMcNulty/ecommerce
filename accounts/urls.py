from django.urls import include, re_path
from . import urls_reset
from .views import index, register, profile, logout, login

urlpatterns = [
    path(r'^register/$', register, name='register'),
    path(r'^profile/$', profile, name='profile'),
    path(r'^logout/$', logout, name='logout'),
    path(r'^login/$', login, name='login'),
    path(r'^password-reset/', include(urls_reset)),
]
