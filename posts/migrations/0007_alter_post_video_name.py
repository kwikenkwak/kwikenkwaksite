# Generated by Django 4.0.1 on 2022-01-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_reddit_link_post_video_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
