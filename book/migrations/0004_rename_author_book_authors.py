# Generated by Django 5.0.5 on 2024-05-09 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_author_alter_book_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]