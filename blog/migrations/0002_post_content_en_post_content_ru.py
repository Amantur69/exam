# Generated by Django 5.0.6 on 2024-06-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='content_ru',
            field=models.TextField(null=True),
        ),
    ]
