# Generated by Django 5.1.1 on 2024-09-25 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="title",
            new_name="gender",
        ),
    ]
