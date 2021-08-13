"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

score = 0
i = 0

# makes temps_inputs file with
name_file = open('temps_input.txt', 'w')
while i < 15:
    print(random.randint(-200, 200), file=name_file)
    i += 1
i = 0
number_of_scores = int(input("Enter number of scores: "))
while i < number_of_scores:
    # generate random number.
    score = random.randint(0, 100)
    # itterate loop
    i += 1
    # use broken_socre to compute score logic.
    if score <= 0:
        print("{} is Invalid score".format(score))
    elif 0 < score < 50:
        print("{} is Bad".format(score))
    elif 50 <= score < 90:
        print("{} is Passable".format(score))
    elif 90 <= score <= 100:
        print("{} is Excellent".format(score))
    else:
        print("{} is Invalid score".format(score))

