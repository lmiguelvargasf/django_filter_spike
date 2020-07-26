from django.db import models
from django.db.models.functions import Length

class BookTitleManager(models.Manager):
    def short_titles(self):
        return self.annotate(length=Length('title')).filter(length__lte=20)

    def long_titles(self):
        return self.annotate(length=Length('title')).filter(length__gt=20, length__lte=30)
    
    def very_long_titles(self):
        return self.annotate(length=Length('title')).filter(length__gt=30)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()

    objects = models.Manager()
    titles = BookTitleManager()

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'
