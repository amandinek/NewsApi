# Generated by Django 2.0.7 on 2020-08-10 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsapp',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='newsapp',
            old_name='decription',
            new_name='description',
        ),
    ]
