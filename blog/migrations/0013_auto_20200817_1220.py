# Generated by Django 3.1 on 2020-08-17 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200817_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenthome',
            name='image',
            field=models.ImageField(blank=True, upload_to='comment'),
        ),
    ]
