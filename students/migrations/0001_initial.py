# Generated by Django 3.0.6 on 2020-05-29 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
