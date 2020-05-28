# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200516_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='slug',
            field=models.SlugField(default='abc-123'),
            preserve_default=False,
        ),
    ]
