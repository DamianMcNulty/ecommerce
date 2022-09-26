from django.urls import re_path as url
from .views import get_todo_list, create_an_item, edit_an_item, toggle_status_todo, vote_todo

urlpatterns = [
    url(r'^$', get_todo_list, name='todo'),
    url(r'^add$', create_an_item),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status_todo),
    url(r'^vote/(?P<id>\d+)$', vote_todo),
    ]