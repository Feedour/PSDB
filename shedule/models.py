from __future__ import unicode_literals
from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Watcher(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    bg = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='images/Watcher/',blank=True)
    info = models.TextField(blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'watchers'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Watcher.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.watcher.save()

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    max_students = models.IntegerField(default=12)
    place = models.CharField(max_length=50, choices=[ ])
    day = models.DateField(default=timezone.now() + timedelta(days=1))
    teacher = models.ForeignKey(Watcher, related_name='teacher_lessons')
    students = models.ManyToManyField(Watcher,related_name='student_lessons', blank=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return 'shedule/%d' % self.pk
    def get_short_count(self):
        return str(self.students.count()) + '/' + str(self.max_students)
    class Meta:
        db_table = 'lessons'
        ordering = ['-day']
