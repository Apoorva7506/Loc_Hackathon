# Generated by Django 3.0.3 on 2020-02-23 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0007_auto_20200222_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='assault',
            name='location',
            field=models.CharField(default=21, max_length=100),
            preserve_default=False,
        ),
    ]
