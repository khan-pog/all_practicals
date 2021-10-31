"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    # Change to desired directory
    os.chdir('FilesToSort')
    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # DONE

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        parts = filename.split('.')
        parts[1]
        print(parts[1])
        # Ignore directories, just process files
        try:
            os.mkdir(parts[1])
        except FileExistsError:
            pass

        shutil.move(filename, parts[1] + '/')
main()
