from django.test import TestCase, Client
from .models import Airport, Flight, Passenger
# Create your tests here.


class FlightTestCase(TestCase):

    def setUp(self):
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        Flight.objects.create(origin=a1, destination=a2, duration=120)
        Flight.objects.create(origin=a1, destination=a1, duration=140)
        Flight.objects.create(origin=a1, destination=a2, duration=180)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 3)

    def test_valid_flight(self):
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")
        f = Flight.objects.get(origin=a1,  destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.create(code="AAA")
        f = Flight.objects.get(origin=a1,  destination=a1)
        self.assertFalse(f.is_valid_flight())
