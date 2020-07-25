import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

class DocumentFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    size = FuzzyInteger(10)
    file_type = FuzzyChoice(['doc', 'txt', 'py', 'png', 'pdf'])

    class Meta:
        model = 'foo.Document'
