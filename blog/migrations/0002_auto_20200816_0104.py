# Generated by Django 3.1 on 2020-08-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslater',
            name='email',
            field=models.CharField(default='admin@gmail.com', max_length=300),
            preserve_default=False,
        ),
    ]
