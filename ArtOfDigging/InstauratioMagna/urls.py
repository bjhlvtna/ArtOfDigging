#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('InstauratioMagna.views',
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[^\.]+)/$',
		view='insta_post_detail',
		name='insta_blog_detail'
	),
	url(r'^page/(?P<page>\w)/$',
		view='insta_post_list',
		name='insta_blog_index_paginated'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
		view='insta_post_archive_day',
		name='insta_blog_archive_day'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
		view='insta_post_archive_month',
		name='insta_blog_archive_month'
	),
	url(r'^(?P<year>\d{4})/$',
		view='insta_post_archive_year',
		name='insta_blog_archive_year'
	),
	url(r'^categories/(?P<slug>[^\.]+)/$',
		view='insta_category_detail',
		name='insta_blog_category_detail'
	),
	url (r'^categories/$',
        view='insta_category_list',
        name='insta_blog_category_list'
    ),
	url(r'^$',
		view='insta_post_list',
		name='insta_blog_index'
	),
)