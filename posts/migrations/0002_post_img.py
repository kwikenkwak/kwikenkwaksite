# Generated by Django 4.0.1 on 2022-01-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.FileField(default='media/default.jpg', upload_to='media/images/'),
            preserve_default=False,
        ),
    ]
