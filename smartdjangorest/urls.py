#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.contrib import admin
from django.urls import include, path, URLPattern, URLResolver
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from smartdjangorest import views, apiviews, settings

import logging

from smartdjangorest.apiviews import api_root

logger = logging.getLogger(__name__)

# API FOR RESOURCES
router = routers.DefaultRouter()
router.register(r'books', apiviews.BookViewSet)


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


urlpatterns = [
    # API RESOURCEFUL VIEWS
    path('api/v1/', include(router.urls), name='book-api'),
    # HTML VIEWS
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('addnewbook', views.addnewbook, name='addnewbook'),
    path('admin/', admin.site.urls),
    path('openapi-schema', get_schema_view(
            title="SmartDjango REST",
            description="API for SmartDjango",
            version="1.0.0"
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger_ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]


urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
logger.info("Installed URLs:")
for p in list_urls(urlconf.urlpatterns):
    logger.info(''.join(p))

