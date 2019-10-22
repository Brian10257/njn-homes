# Generated by Django 2.2.6 on 2019-10-22 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=50000)),
                ('role', models.CharField(blank=True, max_length=500000)),
                ('date_posted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('facebook', models.CharField(blank=True, max_length=50000)),
                ('twitter', models.CharField(blank=True, max_length=50000)),
                ('instagram', models.CharField(blank=True, max_length=50000)),
                ('google_plus', models.CharField(blank=True, max_length=50000)),
                ('linkedin', models.CharField(blank=True, max_length=50000)),
            ],
        ),
    ]