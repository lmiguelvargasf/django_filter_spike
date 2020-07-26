from django.db import models
from django.db.models.functions import Length


class AuthorQuerySet(models.QuerySet):
    def long_first_name(self):
        return self.annotate(length=Length("first_name")).filter(length__gte=10)

    def short_last_name(self):
        return self.annotate(length=Length("last_name")).filter(length__lte=10)


class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def long_first_name(self):
        return self.get_queryset().long_first_name()

    def short_last_name(self):
        return self.get_queryset().short_last_name()


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    objects = AuthorManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
