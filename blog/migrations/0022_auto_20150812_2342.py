# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20150812_2241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navigation',
            options={'ordering': ('order',)},
        ),
        migrations.RenameField(
            model_name='navigation',
            old_name='anchor',
            new_name='target',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 42, 20, 946135, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 42, 20, 938495, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 12, 11, 42, 20, 942482, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=True,
        ),
    ]
