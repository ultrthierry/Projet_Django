# Generated by Django 2.2.7 on 2019-11-22 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='altist',
            new_name='artist',
        ),
    ]