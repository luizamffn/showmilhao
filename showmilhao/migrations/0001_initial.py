# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=100)),
                ('a', models.CharField(max_length=100)),
                ('b', models.CharField(max_length=100)),
                ('c', models.CharField(max_length=100)),
                ('d', models.CharField(max_length=100)),
                ('resposta', models.CharField(max_length=1)),
            ],
        ),
    ]