#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
#
# This is a module written to contain tools used throughout the main program
#         to reduce the duplication of code as the designed moved forward.
#         clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
#                     independent or agnostic.
#         get_data    - Is used for all data entry requests. It used try/except to ensure that the data
#                         entered is the type expected and it also expects a clarifying question or statement.#


#
# Import all required options
#
# Import system and name from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# End of import section

#
# Function definition section of the program
#


def clear():
    # Define the clear function, which is agnostic to the operating system
    # being used. In PyCharm you have to sent "Emulate terminal in output console",
    # which is found under the "Edit run configuration" tab.
    # The clear() module came from https://www.geeksforgeeks.org/clear-screen-python/

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_data(f_i_s, label):
    # Function to request a numerical data, test for validity and
    # return the entered data.
    # f_i_s   - what type of data is requested, (f) for floating point data,
    #         (i) for integer data or (s) for string data.
    # label     - This is the label displayed when requesting data.
    while True:

        if f_i_s == "f":
            # Setup to request data and convert it to a floating point number,
            #   also prepare for invalid data type.
            try:
                entered_data = float(input(label))
            except ValueError:
                print(f"Only numbers are allowed.")
                continue
            break

        elif f_i_s == "i":
            # Setup to request data and convert it to an integer,
            #   also prepare for invalid data type.
            try:
                entered_data = int(input(label))
            except ValueError:
                print(f"Only numbers are allowed.")
                continue
            break

        else:
            # Setup to request string data,
            #   also prepare for invalid data type.
            try:
                entered_data = input(label)
            except ValueError:
                print(f"General warning, expecting letters.")
                continue
            break

    return entered_data

# End of function definitions


# This is set up to all for testing, during development of the
#   tools in the package.
# Test if this is being used as a script?
if __name__ == "__main__":

    # Set the while control value to "Y".
    do_again = "Y"

    # Use while, regarding the desire to re-run the program.
    while do_again != "N":

        # print out some text
        # print('hello geeks\n'*10)

        print("Requesting floating point data")
        data = get_data("f", "Enter floating point data: ")
        print(data)

        print("Requesting integer data")
        data = get_data("i", "Enter integer data: ")
        print(data)

        print("Requesting string data")
        data = get_data("s", "Enter required string: ")
        print(data)

        # sleep for 2 seconds after printing output
        sleep(2)

        # now call function we defined above
        clear()

        # Ask if the user would like to repeat the program.
        # Also, validate for the correct response.
        while True:
            print("\nWould you like to run the program again? Enter (Y) for yes or (N) for no.", end=" ")
            do_again = input().upper()
            if do_again == "N" or do_again == "Y":
                break
            else:
                print("The only valid entries are either a Y or an N.")

# End of Program
