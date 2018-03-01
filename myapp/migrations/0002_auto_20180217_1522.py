# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-17 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rating',
        ),
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(default='game_pic/default-game-n.png', upload_to='game_pic/'),
        ),
    ]