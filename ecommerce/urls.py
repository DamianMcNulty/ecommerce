"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path as url
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT
from issue_tracker import urls as urls_issue_tracker
from todo import urls as urls_todo
from rank import urls as urls_rank

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^rank/', include(urls_rank)),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
    url(r'^issue_tracker/', include(urls_issue_tracker)),
    url(r'^todo/', include(urls_todo)),
]
