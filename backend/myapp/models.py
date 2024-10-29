from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100, default="Неизвестный жанр")

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100, default="Неизвестный раздел")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100, default="Имя")
    last_name = models.CharField(max_length=100, default="Фамилия")
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])

class Cheatsheet(models.Model):
    title = models.CharField(max_length=200, default="Без названия")
    authors = models.ManyToManyField(Author, related_name='cheatsheets')
    genre = models.ManyToManyField(Genre, related_name='cheatsheets')
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='cheatsheets',
        default=1
    )
    year = models.PositiveIntegerField(default=2000)
    file = models.FileField(
        upload_to='cheatsheets/',
        default='cheatsheets/default.pdf',
        blank=True,
        null=True
    )
    cover = models.ImageField(
        upload_to='covers/',
        default='covers/default.png',
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='preference')
    favorite_genres = models.ManyToManyField(Genre, related_name='user_preferences')
    favorite_sections = models.ManyToManyField(Section, related_name='user_preferences')
    favorite_authors = models.ManyToManyField(Author, related_name='user_preferences')
    preferred_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Preferences of {self.user.username}"
