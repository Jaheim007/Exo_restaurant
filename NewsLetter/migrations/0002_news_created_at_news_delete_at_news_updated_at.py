# Generated by Django 4.0.4 on 2022-05-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsLetter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
