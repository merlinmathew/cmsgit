from django.conf.urls import url
from contact import views


__author__ = 'user'

urlpatterns = [
url(r'^contact/', views.contact_view , name='contact'),
]
