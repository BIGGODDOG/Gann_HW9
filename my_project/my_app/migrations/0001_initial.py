# Generated by Django 5.1.1 on 2024-11-02 22:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Ник')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Количество звёзд')),
                ('review', models.TextField(max_length=500, verbose_name='Описание вашего опыта использования приложения')),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Ник')),
                ('rating', models.IntegerField(help_text='Рейтинг от 0 до 100', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Рейтинг книги')),
                ('review', models.TextField(max_length=1000, verbose_name='Рецензия на книгу')),
                ('contains_spoilers', models.BooleanField(default=False, verbose_name='Содержит спойлеры')),
            ],
        ),
    ]
