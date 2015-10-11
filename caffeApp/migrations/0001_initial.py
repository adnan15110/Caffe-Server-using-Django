# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classifierResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('predicted_class', models.CharField(max_length=20)),
                ('image_loaction', models.CharField(max_length=100)),
                ('all_results', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
