# Generated by Django 4.2.7 on 2023-11-30 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist_api', '0003_alter_artist_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='work',
            new_name='works',
        ),
    ]
