# Generated by Django 3.1 on 2020-08-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200816_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likehome',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]