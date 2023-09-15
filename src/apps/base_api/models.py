from django.db import models

# Create your models here.


class EventModel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100)
    cep = models.CharField(max_length=20, null=True)
    date = models.DateTimeField()


class PeopleModel(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    instagram = models.CharField(max_length=20, null=True)


class TransportModel(models.Model):
    company_name = models.CharField(max_length=200)
    number_seats = models.PositiveIntegerField()
    transport_type = models.CharField(max_length=15)


class TripModel(models.Model):
    id_event = models.ForeignKey(
        EventModel, models.DO_NOTHING, related_name="event_trip"
    )
    id_transport = models.ForeignKey(
        TransportModel, models.DO_NOTHING, related_name="transport_trip"
    )
    departure_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    trip_price = models.FloatField(null=True)
    ticket_price = models.FloatField(null=True)


class TicketModel(models.Model):
    id_people = models.ForeignKey(
        PeopleModel, models.DO_NOTHING, related_name="ticket_people"
    )
    link_attach = models.URLField(null=True, max_length=400)
    checked = models.BooleanField(default=False)
    status = models.CharField(max_length=30)
    description = models.TextField(null=True, default=None, blank=True)
