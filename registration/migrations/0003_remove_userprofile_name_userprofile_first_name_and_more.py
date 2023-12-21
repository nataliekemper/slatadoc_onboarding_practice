# Generated by Django 4.2.7 on 2023-12-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0002_userprofile_delete_country_delete_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="name",),
        migrations.AddField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="password",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
