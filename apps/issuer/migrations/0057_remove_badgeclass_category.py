# Generated by Django 2.2.8 on 2020-02-10 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0056_populate_badgeinstance_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badgeclass',
            name='category',
        ),
    ]
