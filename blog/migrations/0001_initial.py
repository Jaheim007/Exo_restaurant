# Generated by Django 4.0.4 on 2022-05-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]