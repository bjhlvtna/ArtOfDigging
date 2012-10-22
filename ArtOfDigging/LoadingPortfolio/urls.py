#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('LoadingPortfolio.views',
	(r'^$', 'index'),
	(r'^(?P<project_slug>.*?)/(?P<video_slug>.*)-video/$', 'video'),
	(r'^(?P<slug>.*)/$', 'detail'),
)
