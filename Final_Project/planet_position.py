#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work on calculating planet positions, based on a requested date.
#   The starting point for this project was https://www.stjarnhimlen.se/comp/ppcomp.html
#       and https://stjarnhimlen.se/comp/tutorial.html#4
#   From this point on, I am converting the code to run in Python.
#
#   This functions returns the Julian Date used for all object location calculations.
#
#
# Import all required items.
#


from kennedy_13 import clear, get_data
""" This is a module written to contain tools used throughout the main program
        to reduce the duplication of code as the designed moved forward.
        clear() - Performs a screen clear using the OS module and is intended to by Operating System (OS)
                    independent or agnostic.
        get_data    - Is used for all data entry requests. It used try/except to ensure that the data
                        entered is the type expected and it also expects a clarifying question or statement. 
"""

from time import perf_counter, perf_counter_ns

"""
Found a reference on this website: https://realpython.com/python-timer/
"""

from datetime import datetime, date, time


from julian_date import julian_date

from menu_builder import menu

from celestial_objects import Object


#
# End of the Import section.
#

"""

Variable List

List info:
    object_list        -   List variable to contain all the celestial data objects entered and allow for the
                            various methods to be applied to them.

String variables:
    In main program:
        do_again    -   Control value for repeating the program.
        command     -   The value entered into the menu system to control the main program.

    In class:
 
Floating point numbers:
    In main program:

    In function:

Integers numbers: 
    In main program:
        command     -   The value entered into the menu system to control the main program.

    In function:

"""

# Set the while control value to "Y".
do_again = "Y"

sky_objects = list()

# Use while, regarding the desire to re-run the program.
while do_again != "N":


    clear()
    print()

    while True:

        command = menu()

        # Retrieve data from the sky objects data file.
        if command == 1:
            with open("sky_data.txt") as sky_data:
                sky_objects.append(sky_data())

        # Write data to the sky objects data file.
        if command == 2:
            with open("sky_data.txt", "a") as sky_data:
                for object in sky_objects:
                    sky_data.write(str(object.info_planet()))


        # List all entered sky objects data.
        if command == 4:
            for object in sky_objects:
                print(object.info_planet())

        # Enter new sky objects data.
        if command == 5:
            sky_objects.append(Object())


        # Gather and print the Julian date.
        if command == 7:
            date = julian_date()

            # Testing the Julian date function
            print(f"\nThe Julian Date & Time for what was entered is: {date:.22f}")

        else:
            break
            # print(f"Your choice was: {command}")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this program again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of Program


# This is set up to all for testing, during development of the
#   tools in the package.
# Test if this is being used as a script?
# if __name__ == "__main__":

