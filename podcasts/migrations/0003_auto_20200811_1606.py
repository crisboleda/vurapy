# Generated by Django 3.1 on 2020-08-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_auto_20200810_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]