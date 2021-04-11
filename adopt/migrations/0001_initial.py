# Generated by Django 3.1.7 on 2021-04-01 15:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caretakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('size', models.DecimalField(decimal_places=1, max_digits=2)),
                ('age', models.PositiveIntegerField(default=0)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('arrival_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('caretaker', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='caretakers.caretaker')),
            ],
        ),
    ]