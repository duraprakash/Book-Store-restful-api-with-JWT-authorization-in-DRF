# Generated by Django 5.0.2 on 2024-05-07 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_buyer_user_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='buyer',
        ),
    ]