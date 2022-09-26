from django.urls import re_path as url
from .views import issue_tracker, create_an_issue, edit_an_issue, toggle_status_issue

urlpatterns = [
    url(r'^$', issue_tracker, name='issue_tracker'),
    url(r'^new_issue$', create_an_issue),
    url(r'^edit_issue/(?P<id>\d+)$', edit_an_issue),
    url(r'^toggle_issue/(?P<id>\d+)$', toggle_status_issue),
    ]
