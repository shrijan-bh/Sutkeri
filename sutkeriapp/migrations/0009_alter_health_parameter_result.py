# Generated by Django 4.1.7 on 2023-03-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutkeriapp', '0008_alter_health_parameter_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_parameter',
            name='Result',
            field=models.CharField(blank='True', max_length=50, null='True'),
        ),
    ]