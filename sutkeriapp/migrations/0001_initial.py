# Generated by Django 4.1.7 on 2023-03-10 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Middle_name', models.CharField(max_length=50, null='True')),
                ('Last_name', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Address', models.CharField(max_length=50)),
                ('Last_period_date', models.DateField()),
            ],
        ),
    ]
