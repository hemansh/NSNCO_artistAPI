# Generated by Django 4.2.7 on 2023-11-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist_api', '0004_rename_work_artist_works'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='works',
            field=models.ManyToManyField(to='artist_api.work'),
        ),
    ]
