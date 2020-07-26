from django.db import models
from django.db.models.functions import Length


class PublisherQuerySet(models.QuerySet):
    def long_name(self):
        return self.annotate(length=Length("name")).filter(length__gte=15)

    def long_address(self):
        return self.annotate(length=Length("address")).filter(length__gte=25)

    def country_starts_with(self, letter):
        return self.filter(country__startswith=letter)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    objects = PublisherQuerySet.as_manager()

    def __str__(self) -> str:
        return self.name
