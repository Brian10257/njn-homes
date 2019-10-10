# Generated by Django 2.2.6 on 2019-10-09 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30000)),
                ('role', models.CharField(blank=True, max_length=30000)),
                ('photo', models.ImageField(blank=True, upload_to='photos/agents/%Y/%m')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=1000)),
                ('email', models.CharField(blank=True, max_length=5000)),
                ('facebook', models.CharField(blank=True, max_length=50000)),
                ('twitter', models.CharField(blank=True, max_length=50000)),
                ('instagram', models.CharField(blank=True, max_length=50000)),
                ('pinterest', models.CharField(blank=True, max_length=50000)),
                ('dribbble', models.CharField(blank=True, max_length=50000)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
