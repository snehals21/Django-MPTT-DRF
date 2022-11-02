from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from rest_framework.response import Response

from .models import Book, Chapter
from rest_framework import viewsets
from .serializers import BookSerializer, ChapterSerializer
from .response import ResponseHandler


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def list(self, request):
        import pdb;pdb.set_trace()
        message = "Listing of chapters"
        response_data = super(ChapterViewSet, self).list(request)
        return ResponseHandler.success(message = message, payload = response_data.data)

    def retrieve(self, request, pk=None):
        message = "Chapter retrieved"
        response_data = super(ChapterViewSet, self).retrieve(request, pk)
        return ResponseHandler.success(message=message,
                                       payload=response_data.data)

    def get_child(self, request, pk=None):
        message = "list children"
        queryset = self.queryset.filter(parent=pk).get_descendants(include_self=True)
        serializer = self.serializer_class(queryset, many=True)
        return ResponseHandler.success(message=message,
                                         payload=serializer.data)

    def get_parent(self, request, pk=None):
        # import pdb;pdb.set_trace()
        message = "list parent"
        queryset = self.queryset.filter(pk=pk).get_ancestors(include_self=False)
        serializer = self.serializer_class(queryset, many=True)
        return ResponseHandler.success(message=message,
                                       payload=serializer.data)




    # import pdb;pdb.set_trace()
    # s = Chapter.objects.filter(pk = 11).get_descendants(include_self = True)
    # Chapter.objects.filter(pk = 11).get_ancestors(include_self = True)

    # def retrieve(self, request, pk=None):
    #     import pdb;pdb.set_trace()
    #     queryset = Chapter.objects.get()
    #     serializer = ChapterSerializer(queryset, pk = pk)
    #     return Response(serializer.data)










