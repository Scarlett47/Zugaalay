# Generated by Django 5.1.3 on 2024-11-19 10:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("venue", "0002_venue_base64image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="venue",
            name="image",
        ),
    ]