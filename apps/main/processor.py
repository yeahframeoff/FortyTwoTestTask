from django.conf import settings


def settings_processor(request):
    gen = ((name, getattr(settings, name))
           for name in dir(settings)
           if not name.startswith('__'))
    settings_dict = dict(gen)
    return {'settings': settings_dict}
