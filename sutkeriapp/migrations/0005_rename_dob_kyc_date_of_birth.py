# Generated by Django 4.1.7 on 2023-03-13 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sutkeriapp', '0004_remove_health_parameter_heart_rate_kyc_husband_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kyc',
            old_name='DOB',
            new_name='Date_of_birth',
        ),
    ]
