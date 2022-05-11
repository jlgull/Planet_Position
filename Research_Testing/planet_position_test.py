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

import pandas

# from menu_builder import menu

# from celestial_objects import Object


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

celestial_csv_data = "Celestial_Objects.csv"

sky_objects = list()

# Use while, regarding the desire to re-run the program.
while do_again != "N":


    clear()
    print()

    """ Compute ecl!
    Another quantity we will need is ecl, the obliquity of the ecliptic, i.e. the "tilt" of the Earth's axis of 
        rotation (currently 23.4 degrees and slowly decreasing). 
        First, compute the "d" of the moment of interest (section 3).
        Then, compute the obliquity of the ecliptic:
        ecl = 23.4393 - 3.563E-7 * d
    """

    d = julian_date()

    """
    Another quantity we will need is ecl, the obliquity of the ecliptic, 
        i.e. the "tilt" of the Earth's axis of rotation (currently 23.4 degrees and slowly decreasing). 
        First, compute the "d" of the moment of interest.
        Then, compute the obliquity of the ecliptic:
        ecl = 23.4393 - 3.563E-7 * d
    """

    ecl_fixed = 23.4393
    ecl_daily = 3.563E-7

    ecl = ecl_fixed - (ecl_daily * d)

    print(f"ecl value: {ecl}")

    celestial_data = pandas.read_csv(celestial_csv_data, index_col=0)



    print(celestial_data["a"])



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

