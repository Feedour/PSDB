from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from PIL import Image

class Planet(models.Model):
    name = models.CharField(max_length=100)
    history = models.TextField()
    image = models.ImageField(upload_to='images/Planet/', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class BG(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    st_nab = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/BG/', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    last_st_nab = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    image = models.ImageField(upload_to='images/Sotrudnik/', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    planet = models.ForeignKey(Planet, null=True, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Mission(models.Model):
    name = models.CharField(max_length=50)
    target = models.TextField()
    history = models.TextField()
    result = models.BooleanField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    planet = models.ForeignKey(Planet, null=True, on_delete=models.SET_NULL)
    bg = models.ForeignKey(BG, null=True, on_delete=models.SET_NULL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

