"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():  # DONE: MOVED ALL INTO MAIN
    """ take user input and output a tempter conversion """
    # variables...

    # statements...
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = converting_celsius_to_fahrenheit(celsius)  # DONE: ADD FUNCTION WHERE OLD CODE WAS
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = converting_fahrenheit_to_celsius(fahrenheit)  # DONE: ADD FUNCTION WHERE OLD CODE WAS
            print("Result: {:.2f} F".format(celsius))
        else:
            print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
    print("Thank you.")


def converting_celsius_to_fahrenheit(celsius):  # DONE: ADDED Converting_celsius_to_fahrenheit
    """Turns celsius to fahrenheit. ouputs fahrenheit"""
    # statements...
    return celsius * 9.0 / 5 + 32


def converting_fahrenheit_to_celsius(fahrenheit):  # DONE: ADDED converting_fahrenheit_to_celsius
    """Turns fahrenheit into celsius. ouputs celsius"""
    # statements...
    return 5 / 9 * (fahrenheit - 32)


main()
