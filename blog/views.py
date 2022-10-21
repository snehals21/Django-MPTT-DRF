from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Book, Chapter
from rest_framework import viewsets
from .serializers import BookSerializer, ChapterSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.root_nodes()



