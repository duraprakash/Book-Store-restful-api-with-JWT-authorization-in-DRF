# Generated by Django 5.0.5 on 2024-05-08 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media')),
                ('isnb', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publication', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('is_available', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Added By')),
                ('author', models.ManyToManyField(to='book.author', verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category', verbose_name='Category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.subcategory', verbose_name='Sub Category')),
            ],
        ),
    ]
