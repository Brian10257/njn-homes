# Generated by Django 2.2.6 on 2019-10-11 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20000)),
                ('email', models.EmailField(max_length=2000)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('subject', models.CharField(blank=True, max_length=500000)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
