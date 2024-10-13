from django.db import models
from django.contrib.auth.models import User

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
    # Дополнительные поля при необходимости

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cheatsheet(models.Model):
    title = models.CharField(max_length=200, default="Без названия")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='cheatsheets',
        default=1  # Временный дефолтный автор с id=1
    )
    genre = models.ManyToManyField(Genre, related_name='cheatsheets')
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='cheatsheets',
        default=1  # Временный дефолтный раздел с id=1
    )
    year = models.PositiveIntegerField(default=2000)
    file = models.FileField(
        upload_to='cheatsheets/',
        default='cheatsheets/default.pdf',  # Временный дефолтный файл
        blank=True,
        null=True
    )
    cover = models.ImageField(
        upload_to='covers/',
        default='covers/default.png',
        blank=True,
        null=True
    )  # Поле для обложки
    description = models.TextField(blank=True, null=True)  # Поле для описания
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Поле для даты загрузки

    def __str__(self):
        return self.title
