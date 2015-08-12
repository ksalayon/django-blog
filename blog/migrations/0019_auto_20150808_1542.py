# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20150807_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 3, 42, 17, 705619, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 3, 42, 17, 696536, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 8, 3, 42, 17, 700647, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
