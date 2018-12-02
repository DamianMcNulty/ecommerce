from django.conf.urls import url
from .views import get_vis

urlpatterns = [
    url(r'^$', get_vis, name='vis'),
    ]