# Generated by Django 3.0.2 on 2020-01-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_auto_20200128_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='upload_file/%Y/%m/%d', verbose_name='파일'),
        ),
    ]
