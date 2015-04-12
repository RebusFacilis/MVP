# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150412_0721'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invenstment',
            new_name='Investment',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='objective',
            new_name='goal',
        ),
    ]
