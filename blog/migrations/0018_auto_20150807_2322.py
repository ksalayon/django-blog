# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20150807_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 11, 22, 12, 571362, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 11, 22, 12, 564479, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 11, 22, 12, 568248, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
