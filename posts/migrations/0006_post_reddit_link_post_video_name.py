# Generated by Django 4.0.1 on 2022-01-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_content_post_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reddit_link',
            field=models.URLField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='video_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
