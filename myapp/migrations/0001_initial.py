# Generated by Django 5.1.2 on 2024-10-13 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Имя', max_length=100)),
                ('last_name', models.CharField(default='Фамилия', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Неизвестный жанр', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Неизвестный раздел', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cheatsheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Без названия', max_length=200)),
                ('year', models.PositiveIntegerField(default=2000)),
                ('file', models.FileField(blank=True, default='cheatsheets/default.pdf', null=True, upload_to='cheatsheets/')),
                ('cover', models.ImageField(blank=True, default='covers/default.png', null=True, upload_to='covers/')),
                ('description', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cheatsheets', to='myapp.author')),
                ('genre', models.ManyToManyField(related_name='cheatsheets', to='myapp.genre')),
                ('section', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cheatsheets', to='myapp.section')),
            ],
        ),
    ]
