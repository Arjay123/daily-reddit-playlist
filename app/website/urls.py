from django.conf.urls import url, include
from website.views import index

urlpatterns = [
    url(r'^$', index, name='index')
]

