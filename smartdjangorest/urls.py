#
#  Project SmartDjango REST
#  Copyright (c) Alessio Saltarin 2021
#  This software is licensed under MIT license
#

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from smartdjangorest import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('addnewbook', views.addnewbook, name='addnewbook'),
    path('api/v1/', include(router.urls)),
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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

