
from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^productlist/$', views.productlist, name='productlist'),
    url(r'^poststock/$', views.poststock, name='poststock'),
    url(r'^postproduct/$', views.postproduct, name='postproduct'),
    url(r'^shelfbarcodecreate/$', views.shelfbarcodecreate, name='shelfbarcodecreate'),
    url(r'^shelfstiker/$', views.shelfstiker, name='shelfstiker'),
    url(r'^productsticker/$', views.productsticker, name='productsticker'),
    url(r'^productstickerbarcode/$', views.productstickerbarcode, name='productstickerbarcode'),
    url(r'^productbarcodecreate/$', views.productbarcodecreate, name='productbarcodecreate'),
    # url(r'^productdetails/$', views.productdetails,name='productdetails'),
    url(r'^search/$', views.search, name='search'),
    url(r'^inspection/$', views.inspection, name='inspection'),
    url(r'^exit/$', views.exit, name='exit'),
    url(r'^barcode/$', views.barcode,name='barcode')


]
