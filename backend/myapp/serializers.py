"""from rest_framework import serializers
from .models import Cheatsheet, Genre, Section, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class CheatsheetSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Cheatsheet
        fields = '__all__'
"""