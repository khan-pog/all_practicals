import random


NUMBEROFRANDOMNUMBERS = 6 # DONE: STORED AS CONSTANTS

QUICKPICKSMAXNUMBER = 45




number_of_pick_picks = int(input("How many qick picks?"))

for i in range(number_of_pick_picks):
    qucik_pick = [0]*NUMBEROFRANDOMNUMBERS

    for number in range(NUMBEROFRANDOMNUMBERS):
        random_number = random.randint(1, QUICKPICKSMAXNUMBER)
        while random_number == qucik_pick[number]:  # DONE:  EACH LINE (QUICK PICK) SHOULD NOT CONTAIN ANY REPEATED NUMBER.
            random_number = random.randint(1, QUICKPICKSMAXNUMBER)
        qucik_pick[number] = random_number
    qucik_pick.sort()   # DONE:  EACH LINE OF NUMBERS SHOULD BE DISPLAYED IN SORTED (ASCENDING) ORDER.
    print(
        f"{qucik_pick[0]:>2}{qucik_pick[1]:>3}{qucik_pick[2]:>3}{qucik_pick[3]:>3}{qucik_pick[4]:>3}{qucik_pick[5]:>3}")
