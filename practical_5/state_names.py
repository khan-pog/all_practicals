""" # DONE: COPPYED THE CODE state_names.py
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# DONE: UPDATE TO UTF-8 FORMATTING
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria",
                "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    # DONE: UPDATE TO NO LONGER REQUIRE CAPITALS
    if state_code.upper() in CODE_TO_NAME:
        print(state_code.upper(), "is", CODE_TO_NAME[state_code.upper()])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
    # DONE: FOR LOOP FIRST DONE ON PAPER THEN ADDED HERE
for state_name in CODE_TO_NAME:
    print(f"{state_name :<3} is {CODE_TO_NAME[state_name]} ")
