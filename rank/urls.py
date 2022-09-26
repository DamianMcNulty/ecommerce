from django.urls import re_path as url
from .views import get_rank

urlpatterns = [
    url(r'^$', get_rank, name='rank'),
    ]