# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150730_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.ImageField(null=True, upload_to=b'post'),
            preserve_default=True,
        ),
    ]
