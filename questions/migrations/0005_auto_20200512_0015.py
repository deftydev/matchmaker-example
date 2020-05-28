# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20200511_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useranswer',
            old_name='their_important',
            new_name='their_importance',
        ),
    ]
