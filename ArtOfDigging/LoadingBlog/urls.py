#-*- coding: utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('LoadingBlog.views',
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[^\.]+)/$',
		view='Loading_post_detail',
		name='Loading_blog_detail'
	),
	url(r'^page/(?P<page>\w)/$',
		view='Loading_post_list',
		name='Loading_blog_index_paginated'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
		view='Loading_post_archive_day',
		name='Loading_blog_archive_day'
	),
	url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
		view='Loading_post_archive_month',
		name='Loading_blog_archive_month'
	),
	url(r'^(?P<year>\d{4})/$',
		view='Loading_post_archive_year',
		name='Loading_blog_archive_year'
	),
	url(r'^categories/(?P<slug>[^\.]+)/$',
		view='Loading_category_detail',
		name='Loading_blog_category_detail'
	),
	url (r'^categories/$',
        view='Loading_category_list',
        name='Loading_blog_category_list'
    ),
	url(r'^$',
		view='Loading_post_list',
		name='Loading_blog_index'
	),
)