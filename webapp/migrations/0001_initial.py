# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=20)),
                ('course_name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=20)),
                ('offered_in_term', models.CharField(max_length=20)),
                ('long_prog', models.BooleanField(default=False)),
                ('core', models.BooleanField(default=False)),
                ('professor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPreference',
            fields=[
                ('bnumber', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=20)),
                ('required_course', models.IntegerField()),
                ('instructor_preference', models.CharField(max_length=50)),
                ('enroll_fulltime', models.BooleanField(default=False)),
                ('comments', models.CharField(max_length=200)),
                ('core_prference_1', models.CharField(max_length=20)),
                ('core_prference_2', models.CharField(max_length=20)),
                ('core_prference_3', models.CharField(max_length=20)),
                ('core_prference_4', models.CharField(max_length=20)),
                ('core_prference_5', models.CharField(max_length=20)),
                ('prefernce_1', models.CharField(max_length=20)),
                ('prefernce_2', models.CharField(max_length=20)),
                ('prefernce_3', models.CharField(max_length=20)),
                ('prefernce_4', models.CharField(max_length=20)),
                ('prefernce_5', models.CharField(max_length=20)),
                ('prefernce_6', models.CharField(max_length=20)),
                ('prefernce_7', models.CharField(max_length=20)),
                ('prefernce_8', models.CharField(max_length=20)),
                ('prefernce_9', models.CharField(max_length=20)),
            ],
        ),
    ]
