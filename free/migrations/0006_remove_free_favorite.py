# Generated by Django 2.1.7 on 2020-08-13 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0005_free_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='free',
            name='favorite',
        ),
    ]
