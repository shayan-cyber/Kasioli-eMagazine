# Generated by Django 3.1 on 2020-09-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20200910_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='thumbnail',
            field=models.ImageField(blank=True, default='20192537-hand-drawn-ink-quill-and-bottle-vector.jpg', upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='ImageTop_optional',
            field=models.ImageField(blank=True, default='20192537-hand-drawn-ink-quill-and-bottle-vector.jpg', upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='thumbnail',
            field=models.ImageField(blank=True, default='20192537-hand-drawn-ink-quill-and-bottle-vector.jpg', upload_to='posts'),
        ),
    ]
