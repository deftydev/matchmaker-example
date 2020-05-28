# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200515_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='text',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
