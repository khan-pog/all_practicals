"""A program that stores users' emails (unique keys) and names (values) in a dictionary."""

email_to_name = {}

email = input("Email: ")
# DONE: ASK THE USER FOR THEIR EMAIL UNTIL THEY ENTER A BLANK ONE.
while email != '':
    parts = email.split("@", 1)
    name_not_formatted = parts[0]
    if '.' in name_not_formatted:
        # DONE: USE A SEPARATE FUNCTION TO GET THE NAME FROM THE EMAIL AS IN THE EXAMPLE BELOW.
        name_formatted = name_not_formatted.split(
            '.')
        name_correct = input(
            "Is your name {} {}? (Y/n)".format(*name_formatted))
        if name_correct == 'n':
            updated_name = input('Name: ')
            email_to_name[email] = updated_name
        elif name_correct == 'Y':
            email_to_name[email] = name_formatted
    else:
        name_formatted = name_not_formatted
        name_correct = input("Is your name {}? (Y/n)".format(name_formatted))
        if name_correct == 'n':
            updated_name = input('Name: ')
            email_to_name[email] = updated_name
        elif name_correct == 'Y':
            email_to_name[email] = name_formatted
    # DONE: JUST LOOP THROUGH THE DICTIONARY (USE THE ITEMS METHOD) AND PRINT THEM OUT.
    email = input("Email: ")
for email, name in email_to_name.items():
    print("{} ({})".format(' '.join(name), email))
