from django.core.management.base import BaseCommand, CommandError
from ...factories import DocumentFactory, BookFactory, AuthorFactory

factories = {
    'Document': DocumentFactory,
    'Book': BookFactory,
    'Author': AuthorFactory
}

class Command(BaseCommand):
    help = 'Creates n instances of Model'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='number of instances')
        parser.add_argument('model', type=str, help='model name')

    def handle(self, *args, **options):
        n = options['n']
        model = options['model']

        if n <= 0:
            raise CommandError('n should be a positive integer')

        try:
            factory = factories[model]
        except KeyError:
            raise CommandError('model does not exist')

        for _ in range(n):
            factory()
        
        self.stdout.write(self.style.SUCCESS(
            f'{n} instance{"s" if n > 1 else ""} of {model} {"were" if n > 1 else "was"} successfully created' )
        )
