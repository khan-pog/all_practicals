number_of_input = 5 # DONE : ASK FOR USER INPUT OF NUMBERS
numbers = []

for i in range(number_of_input):
    numbers.append(input("Number: "))
    numbers[i] = int(numbers[i])


def prints_number_data(numbers, number_of_inputs):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[number_of_inputs - 1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is 20".format(max(numbers)))

    print("The average of the numbers is {}".format((sum(numbers) / len(numbers))))


prints_number_data(numbers, number_of_input)


    # DONE : WOEFULLY INADEQUATE SECURITY CHECKER IMPLEMENTED

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("what is your username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")
