# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import libs.ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=67)),
                ('slug', models.SlugField(unique=True, max_length=100, editable=False, blank=True)),
                ('meta_description', models.CharField(max_length=155, verbose_name=b'Meta description for SEO')),
                ('abstract', models.TextField(max_length=500, verbose_name=b'Abstract (300-500 characters)')),
                ('pub_date', models.DateField(verbose_name=b'Date published')),
                ('keywords', models.CharField(max_length=100, blank=True)),
                ('authors', models.CharField(max_length=100)),
                ('has_latex_formula', models.BooleanField(default=False, verbose_name=b'Post with LATEX formula?')),
                ('content', libs.ckeditor_uploader.fields.RichTextUploadingField(null=True, blank=True)),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
            bases=(models.Model,),
        ),
    ]
