# Generated by Django 2.2.6 on 2019-10-20 04:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30000)),
                ('photo', models.ImageField(upload_to='photos/about/%Y/%m')),
                ('description1', models.TextField(blank=True)),
                ('arreter', models.CharField(blank=True, max_length=50000)),
                ('description2', models.TextField(blank=True)),
                ('description3', models.TextField(blank=True)),
                ('date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
