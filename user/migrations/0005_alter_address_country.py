# Generated by Django 5.0.5 on 2024-05-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_address_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
