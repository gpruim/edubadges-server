# Generated by Django 2.2.9 on 2020-06-04 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0021_populate_institution_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='staff',
            field=models.ManyToManyField(related_name='_institution_staff_+', through='staff.InstitutionStaff', to=settings.AUTH_USER_MODEL),
        ),
    ]