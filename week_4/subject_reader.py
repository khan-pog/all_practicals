"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    #print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    unpacked_file_data = []

    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        unpacked_file_data.append(parts)
    input_file.close()
    return unpacked_file_data   # DONE: Modify the function so it does this. [['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]


def display_subject_details(data):  # DONE: Add a new function to display subject details that produces something like the following:
    """displays subject deails like CP1401 is taught by Ada Lovelace and has 192 students """
    for i in range(4):
        print("{} is taught by {:<12} and has {:>3} students".format(data[i][0], data[i][1], data[i][2]))


main()
