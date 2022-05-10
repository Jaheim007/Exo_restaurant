# Generated by Django 4.0.4 on 2022-05-10 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReseauSocial', '0003_remove_social_created_at_remove_social_delete_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='social',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]