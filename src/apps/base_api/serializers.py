from rest_framework import serializers
from .models import (
    EventModel,
    PeopleModel,
    TripModel,
    TransportModel,
    TicketModel,
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeopleModel
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripModel
        fields = "__all__"


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportModel
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = "__all__"
