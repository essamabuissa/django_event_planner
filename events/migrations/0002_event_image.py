# Generated by Django 2.2.5 on 2020-03-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]
