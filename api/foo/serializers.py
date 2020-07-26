from rest_framework.serializers import ModelSerializer
from rest_framework.utils import field_mapping

from foo.models import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
