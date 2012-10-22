#-*- coding: utf-8 -*-
from django.utils import timezone
from django.db.models import Manager

class PublicManager(Manager):
	def published(self):
		''' Returns any published posts that are available. '''
		return self.get_query_set().filter(publish__lte=timezone.localtime(timezone.now()))