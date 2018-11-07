from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random, datetime
from guestbook.models import TM


def index(request):
    #
    # t = TM.objects.create(talker="someone", message=str(datetime.datetime.now()))
    #
    m = TM.objects.all()
    return render(request, 'FirstView.html', locals())


def talkto(request):
    if request.POST['name'] == "":
        t = TM.objects.create(talker=request.user.username, message=request.POST['msg'])
    else:
        t = TM.objects.create(talker=request.POST['name'], message=request.POST['msg'])

    m = TM.objects.all()
    return render(request, 'FirstView.html', locals())


def back(request):
    #
    # t = TM.objects.create(talker="someone", message=str(datetime.datetime.now()))
    #
    m = TM.objects.all()
    return render(request, 'FirstView.html', locals())


def learn(request):
    return render(request, 'learn.html', locals())


def createpage(request):
    return render(request, 'createpage.html', locals())



