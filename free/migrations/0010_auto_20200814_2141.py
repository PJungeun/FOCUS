# Generated by Django 2.1.7 on 2020-08-14 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0009_auto_20200814_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='free',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='free.Free'),
        ),
    ]