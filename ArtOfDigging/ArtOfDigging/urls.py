#-*- coding: utf-8 -*-
import os
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

media = os.path.join(
	os.path.dirname(__file__),'../media'		
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ArtOfDigging.views.home', name='home'),
    # url(r'^ArtOfDigging/', include('ArtOfDigging.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'ArtOfDigging.views.home'),
    
    (r'^admin/', include(admin.site.urls)),

    (r'^LoadingBlog/', include('LoadingBlog.urls')),
    (r'^DDBlog/', include('DDBlog.urls')),
    (r'^InstauratioMagna/', include('InstauratioMagna.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^LoadingPortfolio/', include('LoadingPortfolio.urls')),    
   	(r'^media/(?P<path>.*)/$','django.views.static.serve', { 'document_root': media }),
)

