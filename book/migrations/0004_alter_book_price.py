# Generated by Django 5.0.5 on 2024-05-12 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]