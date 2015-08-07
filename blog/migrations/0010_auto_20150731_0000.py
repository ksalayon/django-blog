# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150730_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='sub_navigations',
            field=models.ManyToManyField(to='blog.Navigation'),
            preserve_default=True,
        ),
    ]
