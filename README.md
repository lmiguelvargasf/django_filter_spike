# django-filter Spike

The purpose of this "project" is to play around with the library [django-filter][].

## Django Filter

This library is pretty handy for implementing filters based on model's fields.

## SearchFilter

The `SearchFilter` class supports simple single query parameter based searching,
and this is based on the Django admin's search functionality.

This class will only be applied if the view has a `search_fields` attribute set.
The `search_fields` attribute should be a list of names of text type fields on the model,
such as `CharField` or `TextField`.

This will allow the client to filter the items in the list by making queries such as:

```bash
http://example.com/api/users?search=russell
```

For more information see [the docs][searchfilter-docs].

[django-filter]: https://github.com/carltongibson/django-filter
[searchfilter-docs]: https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
