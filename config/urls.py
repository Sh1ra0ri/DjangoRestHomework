from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API для образовательной платформы с курсами и уроками",
        terms_of_service="http://127.0.0.1:8000/terms/",
        contact=openapi.Contact(email="xxnon.7@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url="http://127.0.0.1:8000",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("materials/", include("materials.urls", namespace="materials")),
    path("users/", include("users.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
