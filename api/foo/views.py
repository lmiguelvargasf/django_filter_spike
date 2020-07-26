from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from foo.models import Author, Book, Publisher
from .filters import AuthorFilter, BookFilter
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
