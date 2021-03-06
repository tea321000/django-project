# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-05 13:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='singer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Musician_singer', to='music.Musician'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='birthday',
            field=models.DateTimeField(verbose_name='\u51fa\u751f\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='name',
            field=models.CharField(max_length=40, verbose_name='\u539f\u540d'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='sex',
            field=models.CharField(choices=[('M', '\u7537'), ('F', '\u5973')], max_length=1, verbose_name='\u6027\u522b'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='stagename',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='\u827a\u540d'),
        ),
    ]
