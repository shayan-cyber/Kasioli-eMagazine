# Generated by Django 3.1 on 2020-08-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_likehome_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='likehome',
            name='prk',
            field=models.IntegerField(null=True),
        ),
    ]