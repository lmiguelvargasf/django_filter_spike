from foo.models.book import Book
from rest_framework.serializers import ModelSerializer

from foo.models import Author, Book, Publisher


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
