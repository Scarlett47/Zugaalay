# Generated by Django 5.1.3 on 2024-11-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Venue",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("location", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="venues/"),
                ),
                ("phone", models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
