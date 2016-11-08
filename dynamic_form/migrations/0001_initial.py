# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-08 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('content', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='todo_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='todo_item',
            name='list_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamic_form.todo_list'),
        ),
    ]
