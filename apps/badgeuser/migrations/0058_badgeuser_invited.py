# Generated by Django 2.2.13 on 2020-07-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badgeuser', '0057_auto_20200615_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='badgeuser',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]