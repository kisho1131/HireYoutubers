# Generated by Django 3.2 on 2021-07-12 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='insta_link',
            new_name='linkedIn_link',
        ),
    ]