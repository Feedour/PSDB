from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from PIL import Image


class BG(models.Model):
    name = models.CharField(max_length=200)
    info = models.TextField()
    st_nab = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/BG/', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

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

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


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


class Mission(models.Model):
    name = models.CharField(max_length=50)
    target = models.TextField()
    history = models.TextField()
    result = models.BooleanField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name