#coding:utf8

from django.shortcuts import render, redirect
from page import models

def add_link(request):
	if request.method == 'GET':
		link = models.Link.objects.all().order_by('count', '-date')[:20]
		return render(request, 'add_link.html', {'list': link})
	elif request.method == 'POST':
		add_link_to = request.POST.get('link')
		link = models.Link()
		link.link_to = add_link_to
		link.count = 0
		link.save()
		return redirect('/info/'+str(link.pk))
