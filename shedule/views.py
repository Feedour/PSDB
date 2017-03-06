#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, reverse
from .models import Lesson, Watcher
from django.views import generic
from django.utils import timezone
from django.contrib import messages


def index(request):
    lesson = Lesson.objects.filter(day__day=timezone.now().day).first()
    return HttpResponseRedirect(lesson.pk)


def shedule(request, pk):
    watcher = request.user.watcher;
    delta = timezone.now().hour // 14
    lesson_list = Lesson.objects.filter(day__day=(timezone.now().day + delta))
    context = {'lesson_list':lesson_list,
               'user':watcher,
               'current_lesson':Lesson.objects.get(pk=pk)}
    return render(request, 'shedule/lesson_detail.html', context)


def enroll(request, pk):
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
    return HttpResponseRedirect(reverse('shedule:shedule', args=(pk,)))


class DetailWatcher(generic.DetailView):
    model = Watcher
    template_name = 'shedule/watcher_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailWatcher, self).get_context_data(**kwargs)
        context['user'] = self.request.user.watcher;
        return context
