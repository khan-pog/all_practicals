

import random

number_of_quick_picks = 3
num = 0
number_of_numbers_in_qickpick = 6

for i in range(number_of_quick_picks):
    qucik_pick = []
    for number in range(number_of_numbers_in_qickpick):
        qucik_pick.append(random.randint(1, 45))
    print(f"{qucik_pick[0]:>2}{qucik_pick[1]:>3}{qucik_pick[2]:>3}{qucik_pick[3]:>3}{qucik_pick[4]:>3}{qucik_pick[5]:>3}")

