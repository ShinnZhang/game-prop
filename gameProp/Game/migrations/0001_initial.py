# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-19 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameBase',
            fields=[
                ('game_id', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True, verbose_name='游戏ID')),
                ('game_label', models.CharField(max_length=32, unique=True, verbose_name='游戏名')),
                ('game_neckname', models.CharField(max_length=32, verbose_name='游戏别名')),
                ('game_logo', models.ImageField(upload_to='gameLogos', verbose_name='游戏logo')),
                ('game_op', models.CharField(max_length=128, verbose_name='游戏运行商')),
            ],
            options={
                'db_table': 'game_info_table',
            },
        ),
    ]