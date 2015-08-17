# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20150812_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 10, 28, 21, 548706, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 10, 28, 21, 540727, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 10, 28, 21, 545060, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
