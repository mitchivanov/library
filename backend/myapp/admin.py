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
    list_display = ('title', 'get_authors', 'year', 'section', 'uploaded_at')
    list_filter = ('genre', 'year', 'authors', 'section')
    search_fields = ('title', 'authors__first_name', 'authors__last_name', 'description')
    filter_horizontal = ('genre', 'authors')
    readonly_fields = ('uploaded_at',)

    def get_authors(self, obj):
        return ", ".join([str(author) for author in obj.authors.all()])
    get_authors.short_description = 'Авторы'
