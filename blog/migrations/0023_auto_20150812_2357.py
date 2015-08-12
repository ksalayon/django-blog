# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20150812_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navigation',
            old_name='sub_navigations',
            new_name='subnavigations',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 57, 36, 23912, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 57, 36, 16732, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 57, 36, 20368, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
