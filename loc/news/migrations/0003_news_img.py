# Generated by Django 2.2.6 on 2020-02-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200223_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.TextField(null=True),
        ),
    ]
