#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('DDBlog.views',
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[^\.]+)/$',
		view='dd_post_detail',
		name='dd_blog_detail'
	),
	url(r'^page/(?P<page>\w)/$',
		view='dd_post_list',
		name='dd_blog_index_paginated'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
		view='dd_post_archive_day',
		name='dd_blog_archive_day'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
		view='dd_post_archive_month',
		name='dd_blog_archive_month'
	),
	url(r'^(?P<year>\d{4})/$',
		view='dd_post_archive_year',
		name='dd_blog_archive_year'
	),
	url(r'^categories/(?P<slug>[^\.]+)/$',
		view='dd_category_detail',
		name='dd_blog_category_detail'
	),
	url (r'^categories/$',
        view='dd_category_list',
        name='dd_blog_category_list'
    ),
	url(r'^$',
		view='dd_post_list',
		name='dd_blog_index'
	),
)