# Generated by Django 3.1.7 on 2021-04-08 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210408_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='found',
            name='date',
        ),
    ]
