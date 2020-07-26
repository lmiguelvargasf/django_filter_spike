import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

class DocumentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    size = FuzzyInteger(10)
    file_type = FuzzyChoice(['doc', 'txt', 'py', 'png', 'pdf'])

    class Meta:
        model = 'foo.Document'


class BookFactory(factory.DjangoModelFactory):
    title = factory.Faker('catch_phrase')
    author = factory.Faker('name')
    pages = FuzzyInteger(100, 500, 10)

    class Meta:
        model = 'foo.Book'
