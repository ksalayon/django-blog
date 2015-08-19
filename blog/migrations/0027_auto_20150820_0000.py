# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20150818_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 12, 0, 15, 811265, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 12, 0, 15, 803255, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 12, 0, 15, 807658, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
