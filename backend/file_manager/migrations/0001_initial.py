# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='S3File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('filetype', models.CharField(blank=True, max_length=255)),
                ('s3_filename', models.CharField(max_length=512)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.SET(None), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'S3 File',
                'verbose_name_plural': 'S3 Files',
            },
        ),
    ]