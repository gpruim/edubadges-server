# Generated by Django 2.2.13 on 2020-08-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgeuser', '0066_auto_20200817_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='termsurl',
            name='excerpt',
            field=models.BooleanField(default=False),
        ),
    ]
