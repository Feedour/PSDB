#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .models import Lesson, Watcher
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login


def index(request):
    return HttpResponseRedirect(reverse('shedule:shedule', args=(1,)))


def shedule(request, day):
    return HttpResponseRedirect(reverse('shedule:lesson', args=(1,0)))

def lesson (request, day, pk):
    if (request.user.is_authenticated):
        watcher = request.user.watcher
    else:
        watcher = Watcher(name='Аноним', pk=0)
    day_list = Lesson.objects.fake_day_list()
    lesson_list = Lesson.objects.day_lessons(day)
    current_lesson = lesson_list.filter(pk=pk).first()
    context = {'lesson_list': lesson_list,
               'day_list': day_list,
               'user': watcher,
               'current_lesson': current_lesson,}
    return render(request, 'shedule/shedule.html', context)

def enroll(request, day,pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    watcher = request.user.watcher
    students = lesson.students.all();
    if (lesson.students.count() < lesson.max_students and not students.filter(pk=watcher.pk)):
        if (not lesson.is_specialization):
            previous_lesson = Lesson.objects.filter(name=lesson.name, day__day=(lesson.day.day - 1)).first()
            if (previous_lesson):
                previous_students = previous_lesson.students.all()
                if (previous_students.filter(pk=watcher.pk)):
                    messages.error(request, 'Вы не можете записаться на этот МК т.к. вчера уже были на нем')
            else:
                lesson.students.add(watcher)
                lesson.save()
                messages.success(request, "Готово! Вы записались на это занятие")
        else:
            lesson.students.add(watcher)
            lesson.save()
            messages.success(request, "Готово! Вы записались на это занятие")
    else:
        messages.error(request, 'Вы не можете записаться на этот МК')
    return HttpResponseRedirect(reverse('shedule:lesson', args=(lesson.day,pk,)))

def exit(request):
    logout(request)
    return HttpResponseRedirect(reverse('shedule:login'))

def enter(request):
    if (not request.POST):
        return render(request, 'shedule/signin.html')
    else:
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('shedule:lesson', args=(1, 0)))
        else:
             messages.error(request, 'Неверный логин/пароль')
             return render(request, 'shedule/signin.html')



class DetailWatcher(generic.DetailView):
    model = Watcher
    template_name = 'shedule/watcher_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailWatcher, self).get_context_data(**kwargs)
        context['user'] = self.request.user.watcher;
        return context
