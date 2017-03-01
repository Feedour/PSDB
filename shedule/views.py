#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Lesson, Watcher
from django.views import generic

# Create your views here.
from django.http import HttpResponse

class Menu:
    def __init__(self, name, link):
        self.name = name
        self.link = link
    name = ''
    link = '/archive/'

def index(request, pk):
    watcher = request.user.watcher;
    lesson_list = Lesson.objects.all()
    context = {'lesson_list':lesson_list,
               'watcher':watcher,
               'current_lesson':lesson_list.get(pk=pk)}
    return render(request, 'shedule/lesson_detail.html', context)
class DetailWatcher(generic.DetailView):
    model = Watcher
    template_name = 'shedule/watcher_detail.html'