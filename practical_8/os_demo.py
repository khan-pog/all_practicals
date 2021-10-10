"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # DONE
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # DONE
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    output_name = [100]
    for i, char in enumerate(new_name):
        letters = list(new_name)
        if i > 0:
            if char.isupper() and letters[i-1].islower:
                output_name.append('_')
                output_name.append(char)
            else:
                output_name.append(char)
        else:
            output_name.append(char.upper())
    print(output_name)
    return new_name

def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        for i, filename in enumerate(filenames):
            cucklord = os.path.join(directory_name, filename)
            os.rename(cucklord, os.path.join(directory_name, get_fixed_filename(filename)))

        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

demo_walk()
#main()
