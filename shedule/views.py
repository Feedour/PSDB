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
    watcher = Watcher.objects.get(pk=1)

    menu_list = [Menu(name='Персонал',link='/archive/person/'),
                 Menu(name='Боевые группы', link='/archive/bg/'),
                 Menu(name='Высадки', link='/archive/missions/'),
                 Menu(name='Планеты', link='/archive/planets/'),
                 Menu(name='Расписание', link='/shedule/')]

    lesson_list = Lesson.objects.all()
    context = {'lesson_list':lesson_list,
               'menu_list':menu_list,
               'watcher':watcher,
               'current_lesson':lesson_list.get(pk=pk)}
    return render(request, 'shedule/lesson_detail.html', context)
class DetailWatcher(generic.DetailView):
    model = Watcher
    template_name = 'shedule/watcher_detail.html'