
from django.conf.urls import  include, url
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^productsticker/(?P<id>[0-9a-z-A-Z]+)', views.productsticker,name='productsticker'),
    url(r'^product_barcode/(?P<id>[0-9a-z-A-Z]+)', views.product_barcode,name='product_barcode'),

    url(r'^selfsticker/(?P<id>[0-9a-z-A-Z]+)', views.selfsticker,name='selfsticker'),
    url(r'^self_barcode/(?P<id>[0-9a-z-A-Z]+)', views.self_barcode,name='self_barcode'),

]
