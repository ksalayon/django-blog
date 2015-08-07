# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150804_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='sub_categories',
            field=models.ManyToManyField(to='blog.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='navigation',
            name='sub_navigations',
            field=models.ManyToManyField(to='blog.Navigation', null=True, blank=True),
            preserve_default=True,
        ),
    ]
