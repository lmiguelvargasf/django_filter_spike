from django.db import models

class DocumentManager(models.Manager):
    def pdfs(self):
        return self.filter(file_type='pdf')

    def smaller_than(self, size):
        return self.filter(size__lt=size)


class Document(models.Model):
    name = models.CharField(max_length=30)
    size = models.PositiveIntegerField(default=0)
    file_type = models.CharField(max_length=10, blank=True)

    objects = DocumentManager()

    def __str__(self) -> str:
        return self.name
