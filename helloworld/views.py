from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random, datetime
from guestbook.models import TM
from guestbook.models import Relation, RelationEntry, Concept

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
    concept = Concept.objects.all()
    relation = Relation.objects.all()
    relation_entry = RelationEntry.objects.all()
    return render(request, 'createpage.html', locals())


def newconcept(request):
    dd = Concept.objects.create(title=request.POST["newtitle"], content=request.POST["newcontent"])
    concept = Concept.objects.all()
    relation = Relation.objects.all()
    relation_entry = RelationEntry.objects.all()
    return render(request, 'createpage.html', locals())


def deleteconcept(request, concept_id):
    try:
        to_delete = Concept.objects.get(id=concept_id)
        to_delete.delete()
    except:
        pass
    concept = Concept.objects.all()
    relation = Relation.objects.all()
    relation_entry = RelationEntry.objects.all()
    return render(request, 'createpage.html', locals())


def editconcept(request, concept_id):
    edit_id = concept_id
    concept = Concept.objects.all().order_by('id')
    relation = Relation.objects.all()
    relation_entry = RelationEntry.objects.all()
    return render(request, 'createpage.html', locals())


def editconcept_act(request, concept_id):
    try:
        to_edit = Concept.objects.get(id=concept_id)
        to_edit.title = request.POST["newtitle"]
        to_edit.content = request.POST["newcontent"]
        to_edit.save()
    except:
        pass
    concept = Concept.objects.all().order_by('id')
    relation = Relation.objects.all()
    relation_entry = RelationEntry.objects.all()
    return render(request, 'createpage.html', locals())




