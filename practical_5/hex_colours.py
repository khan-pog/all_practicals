"""
Hexadecimal colour lookup   # DONE: CREATE A PROGRAM THAT ALLOWS YOU TO LOOK UP HEXADECIMAL COLOUR CODES.
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_code = input("colour code: ")
while colour_code != '':  # DONE: ALLOW THE USER TO ENTER NAMES UNTIL THEY ENTER A BLANK ONE TO STOP THE LOOP.
    try:  # DONE: ENTERING AN INVALID COLOUR NAME SHOULD NOT CRASH THE PROGRAM.
        COLOUR_CODES[colour_code]
    except KeyError:
        print("please enter valid colour code")
        colour_code = input("colour code: ")
