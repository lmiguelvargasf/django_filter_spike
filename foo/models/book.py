from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )
    pages = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
