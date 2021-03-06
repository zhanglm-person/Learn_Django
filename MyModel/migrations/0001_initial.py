# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-25 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='\u6807\u9898')),
                ('desprition', models.CharField(blank=True, max_length=255, verbose_name='\u7b80\u4ecb')),
                ('image', models.ImageField(blank=True, upload_to=b'', verbose_name='\u914d\u56fe')),
                ('content', models.TextField(blank=True, verbose_name='\u5185\u5bb9')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u59d3\u540d')),
                ('u_age', models.IntegerField(blank=True, null=True, verbose_name='\u5e74\u9f84')),
                ('u_sex', models.BooleanField(default=True, verbose_name='\u6027\u522b')),
                ('u_position', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u804c\u4f4d')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MyModel.User', verbose_name='\u7528\u6237'),
        ),
    ]
