# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='history',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='history',
            new_name='info',
        ),
        migrations.AddField(
            model_name='bg',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bg',
            name='image',
            field=models.ImageField(upload_to='static/images/BG/', blank=True),
        ),
        migrations.AlterField(
            model_name='bg',
            name='last_st_nab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='archive.Person', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='bg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='archive.BG', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='archive.Planet', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='result',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='static/images/Person/', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='archive.Planet', null=True, blank=True),
        ),
    ]
