from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import View 
# this works for Django==1.9.8 and below i believe so,however Django 1.10 a django.view would suffice 
#Moreover, i would suspect that if you are not using render module for templates, 
#you need to use Django.views.generic
from .models import KirrURL


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
#	print(request.method)
#	try:
#		obj =  KirrURL.objects.get(shortcode = shortcode)
#	except:
#		obj = KirrURL.objects.all().first()
	obj = get_object_or_404(KirrURL, shortcode = shortcode)
#	obj_url = obj.url
	
	
	"""
	obj_url = None
	qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	if qs.exists() and qs.count() == 1 :
		obj = qs.first()
		obj_url = obj.url
	"""
	return HttpResponseRedirect(obj.url)



"""
class KirrCBView(View):
	def get (self, request, *args, **kwargs):
		obj = get_object_or_404(KirrURL, shortcode = shortcode)
		return HttpResponseRedirect(obj.url)
	
	def post (self, request, *args, **kwargs):
		return HttpResponse()
		
"""