# Generated by Django 2.2.7 on 2020-01-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200124_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='picture',
            field=models.URLField(max_length=600, null=True),
        ),
    ]
