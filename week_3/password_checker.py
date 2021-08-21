"""Module docstring"""

# imports
# CONSTANTS
MIN_LENGTH_OF_PASSWORD = 3


def main():  # DONE: ALL INSIDE MAIN FUNCTION
    """Function docstring"""
    # varables...
    password = get_password()


    # statements...
    if len(password) >= MIN_LENGTH_OF_PASSWORD:
        print_asterisk(password)
    else:
        print("the password doesn't meet a minimum length set by a variable.")




def get_password(): #DONE: REFACTORED THE PART THAT GETS THE INPUT FOR PASSWORD
    """Function docstring"""
    # statements...
    return input("Password > ")

def print_asterisk(password): #DONE: REFACTORED THE PART PRINTS THE ASTERISK
    """Function docstring"""
    # statements...
    asterisk_of_length_password = ['*'] * len(password)
    print(*asterisk_of_length_password)


main()
