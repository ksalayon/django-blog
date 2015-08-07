# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150730_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='allow_comment',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
