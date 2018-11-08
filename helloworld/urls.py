"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('users/', include('users.urls')), # new
    path('users/', include('django.contrib.auth.urls')), # new
    url(r'^talkto$', views.talkto, name="talkto"),
    url(r'^back/$', views.back, name="back"),
    url(r'^concept/$', views.createpage, name="createpage"),
    url(r'^learn/$', views.learn, name="learn"),
    url(r'^concept/newconcept/$', views.newconcept, name="newconcept"),
    url(r'^concept/(?P<concept_id>[0-9]+)/delete$', views.deleteconcept, name="deleteconcept"),
    url(r'^concept/(?P<concept_id>[0-9]+)/edit$', views.editconcept, name="editconcept"),
    url(r'^concept/(?P<concept_id>[0-9]+)/edit_act$', views.editconcept_act, name="editconcept_act"),
]
