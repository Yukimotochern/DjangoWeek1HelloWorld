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
    t = TM.objects.create(talker=request.POST['name'], message=request.POST['msg'])
    m = TM.objects.all()
    return render(request, 'FirstView.html', locals())


def fake(request):
    return render(request, 'fake.html')


def back(request):
    #
    # t = TM.objects.create(talker="someone", message=str(datetime.datetime.now()))
    #
    m = TM.objects.all()
    return render(request, 'FirstView.html', locals())