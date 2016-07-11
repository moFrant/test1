"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from view import add_link, info_link, redirect, list_link

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^add/', add_link.add_link),
    url(r'^info/(\w+)$', info_link.info),
    url(r'^red/(\w+)$', redirect.redirect),
    #url(r'^list/del/(\w+)$', 
    url(r'^list/', list_link.list),
    url(r'^del/', list_link.delete),
]
