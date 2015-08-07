# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('type', models.CharField(default=b'external', max_length=8, choices=[(b'external', b'External'), (b'page', b'Page'), (b'post', b'Post')])),
                ('anchor', models.CharField(default=b'_self', max_length=7, choices=[(b'_self', b'Self'), (b'_blank', b'Blank')])),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('sub_navigations', models.ManyToManyField(related_name='sub_navigations_rel_+', to='blog.Navigation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
