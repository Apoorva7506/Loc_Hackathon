# Generated by Django 3.0.3 on 2020-02-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fir', '0002_auto_20200222_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_authenticatedbyp',
            field=models.BooleanField(default=True),
        ),
    ]
