# Managers Spike

The purpose of this "project" is to play around with [Django's Managers][managers].

## Managers

### Custom Manager

I have implemented a custom manager to override the default `Manager`
which can be accessed throught `Model.objects`. ([see logic][custom-manager])

[custom-manager]: ./foo/models.py
[managers]: https://docs.djangoproject.com/en/dev/topics/db/managers/
