# Generated by Django 2.2.7 on 2020-01-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20191122_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='reference',
            field=models.IntegerField(null=True),
        ),
    ]