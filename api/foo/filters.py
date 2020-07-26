from django_filters import rest_framework as filters

from foo.models import Author


class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'email')
