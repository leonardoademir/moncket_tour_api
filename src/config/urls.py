from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.base_api.views import (
    PeopleViewSet,
    TransportViewSet,
    TripViewSet,
    TicketViewSet,
    EventViewSet,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()
router.register("people", PeopleViewSet)
router.register("event", EventViewSet)
router.register("transport", TransportViewSet)
router.register("trip", TripViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

# swagger
urlpatterns += [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),  # noqa E501
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),  # noqa E501
]
