# Generated by Django 5.1.2 on 2024-10-23 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_year', models.PositiveIntegerField(blank=True, null=True)),
                ('favorite_authors', models.ManyToManyField(related_name='user_preferences', to='myapp.author')),
                ('favorite_genres', models.ManyToManyField(related_name='user_preferences', to='myapp.genre')),
                ('favorite_sections', models.ManyToManyField(related_name='user_preferences', to='myapp.section')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]