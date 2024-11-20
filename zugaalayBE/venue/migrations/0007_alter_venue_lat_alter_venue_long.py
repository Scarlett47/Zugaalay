# Generated by Django 5.1.3 on 2024-11-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("venue", "0006_alter_venue_lat_alter_venue_long"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venue",
            name="lat",
            field=models.DecimalField(decimal_places=20, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="venue",
            name="long",
            field=models.DecimalField(decimal_places=20, default=0.0, max_digits=20),
        ),
    ]