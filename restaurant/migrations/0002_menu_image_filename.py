# Generated by Django 4.2.11 on 2025-03-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
