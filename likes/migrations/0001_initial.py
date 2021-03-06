# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('liked_users', models.ManyToManyField(related_name='liked_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(related_name='liker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
