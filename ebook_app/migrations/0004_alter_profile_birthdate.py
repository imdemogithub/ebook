# Generated by Django 4.1 on 2022-08-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ebook_app", "0003_profile_profileimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="BirthDate",
            field=models.DateField(auto_created=True, default="1991-01-01"),
        ),
    ]