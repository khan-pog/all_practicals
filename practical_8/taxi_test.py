"""
CP1404/CP5632 Practical
Car class, test
"""
from practical_8.taxi import Taxi

car = Taxi("Prius 1", 100)
car.drive(40)
print(car)
car.start_fare()
car.drive(100)
print(car)
