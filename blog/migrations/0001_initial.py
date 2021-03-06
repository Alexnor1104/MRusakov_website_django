# Generated by Django 3.2.8 on 2021-12-21 10:49

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Написать заголовок', max_length=70, unique=True, verbose_name='Заголовок')),
                ('slug', models.SlugField(default='', max_length=40, verbose_name='URL')),
                ('content', models.TextField(blank=True, help_text='Напишите текст статьи', verbose_name='Текст статьи')),
                ('photo', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название фото')),
                ('image', models.ImageField(upload_to='images/gallery', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='comments', to='blog.blog')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
