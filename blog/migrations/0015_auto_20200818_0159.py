# Generated by Django 3.1 on 2020-08-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200817_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likepost',
            name='count',
        ),
        migrations.AddField(
            model_name='likepost',
            name='prk',
            field=models.IntegerField(null=True),
        ),
    ]
