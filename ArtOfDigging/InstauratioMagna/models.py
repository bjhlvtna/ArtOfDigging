#-*- coding: utf-8 -*-
import re
import unidecode

from django.db import models
from django.conf import settings
from django.db.models import permalink
from django.template.defaultfilters import slugify
from django.contrib.comments.moderation import CommentModerator, moderator

from string import join
from markdown import markdown
from PIL import Image as PImage
from django.utils import timezone
from os.path import join as pjoin
from sorl.thumbnail import ImageField
from ArtOfDigging.settings import MEDIA_ROOT
from InstauratioMagna.managers import PublicManager


def unidecode_slugify(str):
    str = unidecode.unidecode(str).lower()
    return re.sub(r'\W+','-',str)

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=128)
	slug = models.SlugField(max_length=150, unique=True, editable=False)
	
	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ('title',)

	def __unicode__(self):
		return self.title


	def save(self):
		self.slug = '%s' % slugify(self.title)
		super(Category, self).save()

	@permalink
	def get_absolute_url(self):
	    return ('insta_blog_category_detail', None, {'slug': self.slug})


class Post(models.Model):
	title = models.CharField(max_length=128)
	author = models.CharField(max_length=60)
	body = models.TextField()
	body_html = models.TextField(editable=False, blank=True, null=True)
	publish = models.DateTimeField(default=timezone.localtime(timezone.now()))
	slug = models.SlugField(editable=False, blank=True)
	created = models.DateTimeField(editable=False, default=timezone.localtime(timezone.now()))
	modified = models.DateTimeField(editable=False, auto_now=True)
	categories = models.ManyToManyField(Category, blank=True)
	private = models.BooleanField(default=False)
	objects = PublicManager()

	@permalink
	def get_absolute_url(self):
	    return ('insta_blog_detail', None, {
            'year': self.publish.year,
            'month': self.publish.month,
            'day': self.publish.day,
            'slug': self.slug
        })

	class Meta:
		ordering = ('-publish',)
		get_latest_by = 'publish'

	def save(self):
		self.body_html = markdown(self.body, ['codehilite'])
		self.slug = '%s' % unidecode_slugify(self.title)
		super(Post, self).save()

	def __unicode__(self):
		return self.title

	def get_previous_post(self):
	    return self.get_previous_by_publish()
    
	def get_next_post(self):
	    return self.get_next_by_publish()


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images')
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)  	
    image = ImageField(
    	upload_to='InstauratioMagna/images/',
    )


class File(models.Model):
    post = models.ForeignKey(Post, related_name='files')
    file = models.FileField(
        upload_to='InstauratioMagna/files/'
    )


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.name
