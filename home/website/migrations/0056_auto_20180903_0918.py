# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0055_lecture_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='lector',
        ),
        migrations.AddField(
            model_name='workshop',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='end_time',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workshop',
            name='speakers',
            field=models.ManyToManyField(related_name='workshops', to='website.Speaker'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='speakers',
            field=models.ManyToManyField(related_name='lectures', to='website.Speaker'),
        ),
    ]
