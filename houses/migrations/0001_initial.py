# Generated by Django 4.1.1 on 2022-09-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="House",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
                ("price", models.PositiveBigIntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=140)),
            ],
        ),
    ]
