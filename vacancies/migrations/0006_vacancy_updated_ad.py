# Generated by Django 4.1.2 on 2022-11-21 21:48

from django.db import migrations, models
import vacancies.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_vacancy_min_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='updated_ad',
            field=models.DateField(null=True, validators=[vacancies.models.check_date_no_past]),
        ),
    ]
