# Generated by Django 3.0.2 on 2020-01-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_auto_20200122_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': '공지사항', 'verbose_name_plural': '공지사항'},
        ),
        migrations.AddField(
            model_name='notice',
            name='files',
            field=models.FileField(null=True, upload_to='upload_file/%Y/%m/%d', verbose_name='파일'),
        ),
    ]
