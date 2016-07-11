from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Link(models.Model):
	link_to = models.URLField()
	date = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField()
	
