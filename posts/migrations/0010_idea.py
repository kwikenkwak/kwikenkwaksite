# Generated by Django 4.0.1 on 2022-01-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_reddit_link_post_block_dropper_post_info_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]