from django.urls import re_path as url
from .views import checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    ]