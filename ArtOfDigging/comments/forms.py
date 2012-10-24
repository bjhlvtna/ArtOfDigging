#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.contrib.comments.forms import CommentForm
from django.contrib.contenttypes.models import ContentType

from models import MarkdownComment


class MarkdownCommentForm(CommentForm):
	is_markdown = forms.BooleanField(label=mark_safe('Use <a href="http://en.wikipedia.org/wiki/Markdown">markdown</a> formatting (HTML is not allowed)'), required=False)


	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Name:'
		self.fields['email'].label = 'E-mail:'
		self.fields['comment'].label = 'Comment:'


	def get_comment_model(self):
		return MarkdownComment

	def get_comment_create_data(self):
		#data = super(MarkdownCommentForm, self).get_comment_create_data()
		#data['is_markdown'] = self.cleaned_data['is_markdown']

		return dict(
	        content_type = ContentType.objects.get_for_model(self.target_object),
	        object_pk    = force_unicode(self.target_object._get_pk_val()),
	        user_name    = self.cleaned_data["name"],
	        user_email   = self.cleaned_data["email"],
	        comment      = self.cleaned_data["comment"],
	        submit_date  = timezone.localtime(timezone.now()),
	        site_id      = settings.SITE_ID,
	        is_public    = True,
	        is_removed   = False,
	        is_markdown  = self.cleaned_data["is_markdown"],
    	)

MarkdownCommentForm.base_fields.pop('url')


