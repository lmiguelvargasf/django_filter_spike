from rest_framework.viewsets import ModelViewSet

from foo.models import Author
from .filters import AuthorFilter
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter
