#coding:utf8

from django.shortcuts import render
from page import models
from django.http import HttpResponseRedirect

def redirect(request, offset):
	page = models.Link.objects.get(pk=int(offset))
	count = page.count
	count += 1
	page.count = count
	page.save()
	return HttpResponseRedirect(page.link_to)
