# Generated by Django 4.0.4 on 2022-05-10 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_created_at_about_delete_at_about_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='about',
            name='delete_at',
        ),
        migrations.RemoveField(
            model_name='about',
            name='updated_at',
        ),
    ]