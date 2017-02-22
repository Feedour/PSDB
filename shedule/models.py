from __future__ import unicode_literals
from datetime import timedelta
from django.db import models
from django.utils import timezone
from PIL import Image


class Watcher(models.Model):
    name = models.CharField(max_length=30)
    bg = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='images/Watcher/',blank=True)
    info = models.TextField()
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'watchers'

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    max_students = models.IntegerField(default=12)
    place = models.CharField(max_length=50, choices=[ ])
    day = models.DateField(default=timezone.now() + timedelta(days=1))
    teacher = models.ForeignKey(Watcher, related_name='teacher_lessons')
    students = models.ManyToManyField(Watcher,related_name='student_lessons')
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return 'shedule/%d' % self.pk
    def get_short_count(self):
        return
    class Meta:
        db_table = 'lessons'
        ordering = ['-day']
