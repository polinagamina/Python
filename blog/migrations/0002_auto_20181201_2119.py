# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100)),
                ('Service', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Kind', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegAgreement',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('FIO', models.CharField(max_length=100)),
                ('OI', models.CharField(max_length=100)),
                ('Kind', models.CharField(max_length=100)),
                ('Type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegRequest',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('FIO', models.CharField(max_length=100)),
                ('Service', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=100)),
                ('Service', models.CharField(max_length=100)),
                ('Telephone', models.CharField(max_length=20)),
                ('Email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
