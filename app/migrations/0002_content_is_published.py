# Generated by Django 4.1.3 on 2022-11-05 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]