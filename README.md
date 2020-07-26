# Managers Spike

The purpose of this "project" is to play around with [Django's Managers][managers].

## Managers

### Custom manager overrides default manager

I have implemented a custom manager to override the default `Manager`
which can be accessed throught `Model.objects`. ([see logic][custom-manager])

### Custom manager and default manager

It is possible to have multiple managers for the same model.
I have implemented two custom managers besides the default manager. ([see logic][multiple-managers])

The problem with the previous two approaches is that it is not possible to chain
the methods defined in the managers.

[custom-manager]: ./foo/models/document.py
[managers]: https://docs.djangoproject.com/en/dev/topics/db/managers/
[multiple-managers]: ./foo/models/book.py
