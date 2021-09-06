"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from practical_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, 'my_car')
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    limo = Car(100, 'limo')     # Done.
    limo.add_fuel(20)   # Done.
    print(limo.fuel)  # Done.
    limo.drive(115)  # Done.
    print(limo.odometer)  # Done.
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()