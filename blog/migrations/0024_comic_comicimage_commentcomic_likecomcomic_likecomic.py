# Generated by Django 3.1 on 2020-09-09 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_remove_author_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='posts')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('xonkhya', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.xonkhya')),
            ],
        ),
        migrations.CreateModel(
            name='Commentcomic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='comment')),
                ('time', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comic')),
            ],
        ),
        migrations.CreateModel(
            name='Likecomic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prk', models.IntegerField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comic')),
            ],
        ),
        migrations.CreateModel(
            name='Likecomcomic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prk', models.IntegerField(null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.commentcomic')),
            ],
        ),
        migrations.CreateModel(
            name='ComicImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts')),
                ('comic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.comic')),
            ],
        ),
    ]
