# Generated by Django 4.0.1 on 2022-01-22 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_img_post_img_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='upload_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
