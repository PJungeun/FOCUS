# Generated by Django 2.1.7 on 2020-08-14 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0011_auto_20200814_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='free',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='free',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
