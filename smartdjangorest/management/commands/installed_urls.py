#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#
import logging

from django.core.management import BaseCommand
from django.urls import URLPattern, URLResolver

from smartdjangorest import settings

#
# This command is run by
# 'python manage.py installed_urls'
#
logger = logging.getLogger(__name__)


def list_urls(lis, acc=None):
    """
    List installed URLs
    """
    if acc is None:
        acc = []
    if not lis:
        return
    first_list = lis[0]
    if isinstance(first_list, URLPattern):
        yield acc + [str(first_list.pattern)]
    elif isinstance(first_list, URLResolver):
        yield from list_urls(first_list.url_patterns, acc + [str(first_list.pattern)])
    yield from list_urls(lis[1:], acc)


class Command(BaseCommand):
    args = ''
    help = 'Lists the currently available URLS'

    def handle(self, *args, **options):
        logger.info("Installed URLs:")
        urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
        for p in list_urls(urlconf.urlpatterns):
            logger.info(''.join(p))

