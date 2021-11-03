"""
CP1404/CP5632 Practical
Test silver service taxi class
"""
from practical_8.silver_service_taxi import SilverServiceTaxi

car = SilverServiceTaxi("name", 100, 2)
car.start_fare()
car.drive(18)
print(car)
