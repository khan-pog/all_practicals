"""
CP1404/CP5632 Practical
Car class
"""
from practical_8.taxi import Taxi
import random

class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        Taxi.self.price_per_km = Taxi.self.price_per_km * fanciness
        self.current_fare_distance = 0
        self.flagfall = 4.5

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{},  ${:.2f}/km plus flagfall of ${}".format(super().__str__(),
                                                             self.Taxi.price_per_km,
                                                             self.flagfall)
