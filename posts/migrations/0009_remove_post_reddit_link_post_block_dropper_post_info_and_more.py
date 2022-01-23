# Generated by Django 4.0.1 on 2022-01-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_video_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reddit_link',
        ),
        migrations.AddField(
            model_name='post',
            name='block_dropper',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='info',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(),
        ),
    ]
