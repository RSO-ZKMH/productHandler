from django.contrib import admin
from django.urls import path

from products.views import ProductViewSet
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi
import os
from drf_yasg.generators import OpenAPISchemaGenerator


class PublicAPISchemeGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        # Get env variable
        base_path = os.getenv('BASE_PATH', '')
        schema.base_path = base_path+'/api/v1'
        return schema


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Products API",
        default_version='1.0.0',
        description="API Documentation for products",
        url="http://localhost:8000"
    ),
    public=True,
    generator_class=PublicAPISchemeGenerator
)

"""
schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Products API",
        default_version='1.0.0',
        description="API Documentation for products",
        url="http://localhost:9000"
    ),
    public=True
)
"""
urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
        'patch': 'partial_update',
    })),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
