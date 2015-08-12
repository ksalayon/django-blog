# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20150808_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 10, 38, 39, 996557, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 10, 38, 39, 988999, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 10, 38, 39, 992830, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
