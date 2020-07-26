from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
