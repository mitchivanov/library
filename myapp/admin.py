from django.contrib import admin
from .models import Cheatsheet, Genre, Section, Author

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

@admin.register(Cheatsheet)
class CheatsheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'section', 'uploaded_at')
    list_filter = ('genre', 'year', 'author', 'section')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'description')
    filter_horizontal = ('genre',)
    readonly_fields = ('uploaded_at',)  # Сделать поле даты загрузки только для чтения
