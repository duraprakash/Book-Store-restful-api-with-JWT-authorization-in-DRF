# Generated by Django 5.0.5 on 2024-05-10 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_address_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.geo', verbose_name='Geo'),
        ),
    ]