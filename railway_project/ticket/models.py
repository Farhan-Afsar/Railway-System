from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    capacity = models.IntegerField()

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Station(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)

class Route(models.Model):
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='route_origin')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='route_destination')
    distance = models.FloatField()

class Schedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='ticket')

# Add this line after the Ticket model
Passenger.ticket = models.OneToOneField(Ticket, on_delete=models.SET_NULL, null=True, related_name='passenger')
