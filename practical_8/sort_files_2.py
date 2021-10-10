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

    type_to_dir = {}
    for i, filename in enumerate(os.listdir('.')):
        if os.path.isdir(filename):
            continue
        parts_file_type = filename.split(".")
        type_to_dir[parts_file_type[1]] = ""
    for file_type in type_to_dir.keys():
        directorty = input("What category would you like to sort {} files into?".format(file_type))
        type_to_dir[file_type] = directorty
        try:
            os.mkdir(type_to_dir[file_type])
        except FileExistsError:
            pass
    for i, filename in enumerate(os.listdir('.')):
        if os.path.isdir(filename):
            continue
        for type in type_to_dir:
            try:
                shutil.move(filename, type_to_dir[type])
            except:
                pass
    print(type_to_dir)

main()