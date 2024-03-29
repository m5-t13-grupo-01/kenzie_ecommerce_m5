# Generated by Django 4.1.7 on 2023-03-09 17:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("city", models.CharField(max_length=127)),
                ("street", models.CharField(max_length=127)),
                ("number", models.SmallIntegerField()),
                ("zip_code", models.CharField(max_length=8)),
                ("state", models.CharField(max_length=2)),
            ],
        ),
    ]
