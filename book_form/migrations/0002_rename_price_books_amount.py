# Generated by Django 4.0.2 on 2022-03-14 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='price',
            new_name='amount',
        ),
    ]
