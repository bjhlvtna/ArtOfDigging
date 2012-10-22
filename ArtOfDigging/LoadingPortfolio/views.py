#-*- coding: utf-8 -*-
# Create your views here.
from itertools import chain
from django.template import RequestContext
from LoadingPortfolio.models import Project, Video
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
	all_projects = Project.objects.all().filter(published=True).order_by('category', '-start_date')
	return render_to_response('LoadingPortfolio/index.html', locals(), context_instance=RequestContext(request))
	
def detail(request, slug):
	project = get_object_or_404(Project, slug=slug, published=True)
	return render_to_response('LoadingPortfolio/detail.html', locals(), context_instance=RequestContext(request))
	
def video(request, project_slug, video_slug):
	project = get_object_or_404(Project, slug=project_slug, published=True)
	video = get_object_or_404(Video, project=project, slug=video_slug)
	return render_to_response('LoadingPortfolio/video.html', locals(), context_instance=RequestContext(request))
