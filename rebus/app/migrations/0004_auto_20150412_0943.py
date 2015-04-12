# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150412_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='objective',
            new_name='goal',
        ),
    ]
