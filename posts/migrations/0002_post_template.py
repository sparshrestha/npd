# Generated by Django 3.0.6 on 2020-05-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='template',
            field=models.FileField(default=None, upload_to='images/'),
        ),
    ]