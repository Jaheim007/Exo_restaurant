# Generated by Django 4.0.4 on 2022-05-10 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0002_siteinfo_created_at_siteinfo_delete_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteinfo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='delete_at',
        ),
        migrations.RemoveField(
            model_name='siteinfo',
            name='updated_at',
        ),
    ]