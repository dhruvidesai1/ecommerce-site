# Generated by Django 5.2.3 on 2025-07-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.CharField(default="1", max_length=200),
            preserve_default=False,
        ),
    ]
