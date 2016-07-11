#coding:utf8

from django.shortcuts import render, redirect
from page import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list(request):
	links = models.Link.objects.all().order_by('count', '-date')
	try:
		pages = Paginator(links, 1)
		page_num = request.GET.get('page')
		try:
			page = pages.page(page_num)
		except PageNotAnInteger:
			page = pages.page(1)
		except EmptyPage:
			page = pages.page(pages.num_pages)
	
		return render(request, 'list.html', {"content": page.object_list[0], 'content1': page})
	except:
		return redirect('/add/')
	
def delete(request):
	link = models.Link.objects.get(pk=int(request.GET.get('pk'))).delete()
	return redirect('/list/?page='+request.GET.get('pk'))
