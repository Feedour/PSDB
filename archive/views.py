# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import BG
from .models import Planet
from .models import Person
from .models import Mission
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse


def index(request):
    return HttpResponseRedirect(reverse('archive:bg', args=(1,)))


def index_person(request):
    return HttpResponseRedirect(reverse('archive:person', args=(1,)))


def index_bg(request):
    return HttpResponseRedirect(reverse('archive:bg', args=(1,)))


def index_planet(request):
    return HttpResponseRedirect(reverse('archive:planet', args=(1,)))


def index_mission(request):
    return HttpResponseRedirect(reverse('archive:mission', args=(1,)))


def person(request,pk):
    person_list=Person.objects.all();
    if person_list.filter(pk=pk):
        current_person = Person.objects.get(pk=pk)
    else:
        current_person = person_list.first()
    context = {'Person_list':person_list,
               'current_person':current_person}
    return render(request, 'archive/people.html', context)


def bg(request, pk):
    bg_list = BG.objects.all();
    if bg_list.filter(pk=pk):
        current_bg = BG.objects.get(pk=pk)
    else:
        current_bg = bg_list.first()
    context = {'BG_list': bg_list,
               'current_bg': current_bg}
    return render(request, 'archive/bg.html', context)


def planet(request,pk):
    planet_list=Planet.objects.all();
    if planet_list.filter(pk=pk):
        current_planet=Planet.objects.get(pk=pk)
    else:
        current_planet=planet_list.first()
    context = {'Planet_list': planet_list,
               'current_planet': current_planet}
    return render(request, 'archive/planet.html', context)


def mission(request,pk):
    mission_list=Mission.objects.all();
    if mission_list.filter(pk=pk):
        current_mission=Mission.objects.get(pk=pk)
    else:
        current_mission=mission_list.first()
    context = {'Mission_list': mission_list,
               'current_mission': current_mission}
    return render(request, 'archive/mission.html', context)
