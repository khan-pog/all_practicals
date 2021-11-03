"""
CP1404/CP5632 Practical
Car class
"""
from practical_6.car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability
        self.random_number = random.randint(0, 100)

    def __str__(self):
        """Return a string like a Car but with reliability data distance."""
        return "{} {} {}".format(super().__str__(), self.reliability, self.random_number)

    def drive(self, distance):
        """Drive like parent Car but also do reliability check."""
        distance_driven = 0
        if self.random_number > self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
