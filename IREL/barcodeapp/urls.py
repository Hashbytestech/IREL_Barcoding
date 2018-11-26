
from django.conf.urls import url
from django.contrib import admin
from .import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^poststock/$', views.poststock,name='poststock'),
    url(r'^postproduct/$', views.postproduct,name='postproduct'),
    url(r'^shelfsticker/$', views.shelfstiker,name='shelfsticker'),
    url(r'^shelfbarcodecreate/$', views.shelfbarcodecreate,name='shelfbarcodecreate'),
    url(r'^productsticker/$', views.productsticker,name='productsticker'),
    url(r'^productbarcodecreate/$', views.productbarcodecreate,name='productbarcodecreate'),
    # url(r'^productdetails/$', views.productdetails,name='productdetails'),
    url(r'^search/$', views.search, name='search'),
]
