# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_pages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('feature_image', models.ImageField(upload_to=b'post')),
                ('content', models.TextField()),
                ('allow_comment', models.BooleanField()),
                ('created', models.DateTimeField(verbose_name=b'date published')),
                ('modified', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='create',
            new_name='created',
        ),
    ]
