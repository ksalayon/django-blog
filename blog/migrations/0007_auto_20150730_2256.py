# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150730_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='modified',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
