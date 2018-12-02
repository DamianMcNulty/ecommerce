from django.conf.urls import url
from .views import get_rank

urlpatterns = [
    url(r'^$', get_rank, name='rank'),
    ]