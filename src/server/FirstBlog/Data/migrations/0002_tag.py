# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('person', models.OneToOneField(related_name='personModel', primary_key=True, serialize=False, to='Data.data')),
                ('age_group', models.CharField(max_length=6, choices=[(b'K', b'KIDS'), (b'A', b'ADULT'), (b'S', b'SENIOR')])),
            ],
        ),
    ]
