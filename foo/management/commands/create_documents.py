from django.core.management.base import BaseCommand, CommandError
from ...factories import DocumentFactory

class Command(BaseCommand):
    help = 'Creates n Document instances'

    def add_arguments(self, parser):
        parser.add_argument('n', type=int, help='number of instances')

    def handle(self, *args, **options):
        n = options['n']

        if n <= 0:
            raise CommandError('n should be a positive integer')

        for _ in range(n):
            DocumentFactory()
        self.stdout.write(self.style.SUCCESS(f'{n} instance{"s were" if n > 1 else " was"} successfully created' ))
