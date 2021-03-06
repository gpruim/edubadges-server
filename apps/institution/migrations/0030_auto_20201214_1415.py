# Generated by Django 2.2.13 on 2020-12-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0029_description_multi_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='description',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='description',
        ),
        migrations.AlterField(
            model_name='institution',
            name='grondslag_formeel',
            field=models.CharField(choices=[('uitvoering_overeenkomst', 'uitvoering_overeenkomst'), ('gerechtvaardigd_belang', 'gerechtvaardigd_belang'), ('wettelijke_verplichting', 'wettelijke_verplichting')], default='uitvoering_overeenkomst', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='grondslag_informeel',
            field=models.CharField(choices=[('uitvoering_overeenkomst', 'uitvoering_overeenkomst'), ('gerechtvaardigd_belang', 'gerechtvaardigd_belang'), ('wettelijke_verplichting', 'wettelijke_verplichting')], default='uitvoering_overeenkomst', max_length=254, null=True),
        ),
    ]
