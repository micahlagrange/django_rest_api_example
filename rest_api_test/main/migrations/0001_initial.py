# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=200)),
                ('mail', models.EmailField(null=True, max_length=254)),
                ('blurb', models.TextField(null=True)),
            ],
        ),
    ]
