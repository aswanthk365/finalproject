# Generated by Django 5.0.2 on 2024-03-06 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0007_rename_raiting_reviewrating_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewRating',
        ),
    ]
