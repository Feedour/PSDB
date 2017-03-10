# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import BG
from .models import Planet
from .models import Person
from .models import Mission
from django.http import HttpResponse


def index(request):
    return render(request, 'main.html', {})


def person(request,pk):
    person_list=Person.objects.all();
    context = {'Person_list':person_list,
               'current_person':Person.objects.get(pk=pk)}
    return render(request, 'archive/people.html', context)


def bg(request, pk):
    bg_list = BG.objects.all();
    context = {'BG_list': bg_list,
               'current_bg': BG.objects.get(pk=pk)}
    return render(request, 'archive/bg.html', context)


def planet(request,pk):
    planet_list=Planet.objects.all();
    context = {'Planet_list': planet_list,
               'current_planet': Planet.objects.get(pk=pk)}
    return render(request, 'archive/planet.html', context)


def mission(request,pk):
    mission_list=Mission.objects.all();
    context = {'Mission_list': mission_list,
               'current_mission': Mission.objects.get(pk=pk)}
    return render(request, 'archive/mission.html', context)
