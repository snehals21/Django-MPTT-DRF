from .models import Book, Chapter
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    # children = RecursiveField(many = True)

    class Meta:
        model = Chapter
        fields = ['id', 'book', 'name', 'parent', 'level', 'publish', 'children']

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = ChapterSerializer(many = True)
        return fields
