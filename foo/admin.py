from django.contrib import admin

from .models import Document, Book, Author, Publisher


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'file_type')

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
