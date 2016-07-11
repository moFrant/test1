#coding:utf8

from django.shortcuts import render, redirect
from page import models

def info(request, offset):
	page = models.Link.objects.get(pk=int(offset))
	return render(request, 'info.html', {'origional_link': page.link_to, 'link': 'yodaweb.ru/red/'+str(page.pk), 'count': str(page.count), 'date': page.date})
