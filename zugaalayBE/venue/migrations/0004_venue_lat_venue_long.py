# Generated by Django 5.1.3 on 2024-11-19 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venue", "0003_remove_venue_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="venue",
            name="lat",
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name="venue",
            name="long",
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=9),
        ),
    ]
