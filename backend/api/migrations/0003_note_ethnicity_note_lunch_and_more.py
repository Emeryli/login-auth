# Generated by Django 5.1.1 on 2024-09-25 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_rename_title_note_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="ethnicity",
            field=models.CharField(default="Not Specified", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="lunch",
            field=models.CharField(default="Not Specified", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="parental_level_of_education",
            field=models.CharField(default="Not Specified", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="reading_score",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="test_preparation_course",
            field=models.CharField(default=0.0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="note",
            name="writing_score",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]
