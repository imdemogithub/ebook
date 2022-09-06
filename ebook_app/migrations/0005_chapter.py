# Generated by Django 4.1 on 2022-09-06 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ebook_app", "0004_alter_profile_birthdate"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chapter",
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
                ("ChapterName", models.CharField(max_length=100)),
                ("ChapterNumber", models.IntegerField()),
                ("Content", models.FileField(upload_to="book_chapters/")),
                ("UpdatedDate", models.DateTimeField(auto_now=True)),
                (
                    "Book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ebook_app.book"
                    ),
                ),
            ],
            options={"db_table": "chapter",},
        ),
    ]
