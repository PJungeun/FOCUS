# Generated by Django 2.1.7 on 2020-08-14 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('free', '0008_remove_free_like_user_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='free',
            name='like_user_set',
            field=models.ManyToManyField(blank=True, related_name='like_user_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='free',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='free.Free', verbose_name='좋아요'),
        ),
    ]
