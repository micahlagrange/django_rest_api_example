# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restuser',
            name='blurb',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='restuser',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
