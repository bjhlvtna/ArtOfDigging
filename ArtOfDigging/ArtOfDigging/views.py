from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
	return HttpResponseRedirect(reverse('LoadingBlog.views.post_list'))
	