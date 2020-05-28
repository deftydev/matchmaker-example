# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20200515_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
