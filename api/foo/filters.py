from django_filters import rest_framework as filters

from foo.models import Author, Book


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = ("first_name", "last_name", "email")


class BookFilter(filters.FilterSet):
    min_pages = filters.NumberFilter(field_name='pages', lookup_expr='gte')
    class Meta:
        model = Book
        fields = ("title",)
