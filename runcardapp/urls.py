from django.urls import re_path as url
from runcardapp.views import runcardpage

urlpatterns = [
    url('', runcardpage, name='runcardpage'),
]