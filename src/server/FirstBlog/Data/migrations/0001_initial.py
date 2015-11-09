# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=6, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField()),
                ('active', models.BooleanField()),
                ('tags', models.TextField()),
            ],
        ),
    ]
