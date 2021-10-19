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
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from smartdjangorest import views, apiviews, settings

# API FOR RESOURCES
router = routers.DefaultRouter()
router.register(r'books', apiviews.BookViewSet)

urlpatterns = [
    # JWT TOKENS
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API RESOURCEFUL VIEWS
    path('api/v1/', include(router.urls), name='book-api'),
    # HTML VIEWS
    path('', views.index, name='index'),
    path('books', views.books, name='books'),
    path('addnewbook', views.addnewbook, name='addnewbook'),
    path('admin/', admin.site.urls),
    path('openapi-schema', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]



