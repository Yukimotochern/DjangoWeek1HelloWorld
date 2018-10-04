from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random, datetime


def index(request):
    random.seed(str(datetime.datetime.now()))
    random_list = [random.randint(0, 1088) for _ in range(20)]
    context = {'random_list': random_list}
    return render(request, 'FirstView.html', context)
