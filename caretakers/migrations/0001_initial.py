# Generated by Django 3.1.7 on 2021-04-01 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.PositiveIntegerField(default=0)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('phone', models.IntegerField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]