# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-20 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viruses', '0002_auto_20180720_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='sequence',
            name='sequence_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viruses.Virus'),
        ),
    ]
