from apps.base_api.serializers import (
    EventSerializer,
    TransportSerializer,
    TripSerializer,
    PeopleSerializer,
    TicketSerializer,
)
from .models import (
    EventModel,
    TransportModel,
    TripModel,
    PeopleModel,
    TicketModel,
)
from rest_framework.viewsets import ModelViewSet


class EventViewSet(ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
    http_method_names = ["post", "get", "patch"]


class TransportViewSet(ModelViewSet):
    queryset = TransportModel.objects.all()
    serializer_class = TransportSerializer
    http_method_names = ["post", "get", "patch"]


class TripViewSet(ModelViewSet):
    queryset = TripModel.objects.all()
    serializer_class = TripSerializer
    http_method_names = ["post", "get", "patch"]


class PeopleViewSet(ModelViewSet):
    queryset = PeopleModel.objects.all()
    serializer_class = PeopleSerializer
    http_method_names = ["post", "get", "patch"]


class TicketViewSet(ModelViewSet):
    queryset = TicketModel.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ["post", "get", "patch"]
