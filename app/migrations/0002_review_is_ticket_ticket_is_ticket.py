# Generated by Django 4.2.4 on 2023-08-26 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="is_ticket",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ticket",
            name="is_ticket",
            field=models.BooleanField(default=True),
        ),
    ]