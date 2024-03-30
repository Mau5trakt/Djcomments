# Generated by Django 5.0.3 on 2024-03-29 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('comment_text', models.CharField(max_length=140)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2024, 3, 29, 15, 57, 39, 35238))),
            ],
        ),
    ]
