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

from datetime import date, time
""" 
This imports the date and time methods from the datetime module.
"""

#
# End of the Import section.
#

"""
Here are the developmental notes from: https://stjarnhimlen.se/comp/tutorial.html
    In all the notes "d" is used for the Julian date value; but for the program "julian_date" was used. 
    This will also be true in the main body of the program

The time scale in these formulae are counted in days. Hours, minutes, seconds are expressed as fractions of a day.
    Day 0.0 occurs at 2000 Jan 0.0 UT (or 1999 Dec 31, 0:00 UT). This "day number" d is computed as follows
    (y=year, m=month, D=date, UT=UT in hours+decimals):
    d = 367*y - 7 * ( y + (m+9)/12 ) / 4 + 275*m/9 + D - 730530
        Note that the formula above is only valid from March 1900 to February 2100.
Below is another formula, which is valid over the entire Gregorian Calendar:
    d = 367*y - 7 * ( y + (m+9)/12 ) / 4 - 3 * ( ( y + (m-9)/7 ) / 100 + 1 ) / 4 + 275*m/9 + D - 730515
Note that ALL divisions here should be INTEGER divisions. In Pascal, use "div" instead of "/", in MS-Basic,
    use "\" instead of "/". In Fortran, C and C++ "/" can be used if both y and m are integers. 
    In Python use "//" to ensure INTEGER division is used to arrived at the base Julian date.
    Finally, include the time of the day, by adding:
    d = d + UT/24.0        (this is a floating-point division)

This function was developed using the second date formula above. It can be tested using the follow
    test data.
    
    Test Date: compute d for 19 april 1990, at 0:00 UT 
                Result is -3543.0000000 
"""


def julian_date():

    # Collect the birthday information.
    # Using try-except to ensure date entry values are valid.
    while True:
        try:
            birth_day = date(int(input("Enter year: ")), int(input("Enter month: ")), int(input("Enter day: ")))
        except ValueError:
            print("Only 1 to 12 for month entry and 1 to 31 for day entry.")
            continue
        break

    # Collect the Birth time information.
    # Using try-except to ensure date entry values are valid.
    while True:
        try:
            birth_time = time(int(input("Enter hour: ")), int(input("Enter minute: ")))
        except ValueError:
            print("Only 0 to 23 for hour entry and 0 to 59 for minute entry..")
            continue
        break

    # Convert the entered birth time to a decimal value.
    birth_time_decimal = birth_time.hour + (birth_time.minute + birth_time.second/60)/60

    # Calculate the julian date, using the more complex formula, see comments above.
    j_date = 367 * birth_day.year - 7 * (birth_day.year + (birth_day.month + 9) // 12) // 4 \
        - 3 * ((birth_day.year + (birth_day.month - 9) // 7) // 100 + 1) // 4 \
        + 275 * birth_day.month // 9 + birth_day.day - 730515

    final_j_date = j_date + birth_time_decimal/24

    return final_j_date


# This is set up to all for testing, during development of the
#   tools in the package.
# Test if this is being used as a script?
if __name__ == "__main__":

    clear()
    print()

    julian_date = julian_date()

    """
    
    These print commands were removed from the function, after it was functional. To use them, they would have 
        place back in the definition of the function.
        
    print(f"\nEntered day was: {birth_day}")
    
    print(f"Entered time was: {birth_time} or {birth_time_decimal:0.12f}")
    
    print(f"\nJulian Date = {julian_date}")
   
    print(f"\nEntered day was: {birth_day} and the time was {birth_time.hour:02d}:{birth_time.minute:02d}.")
   
    """

    print(f"The final Julian Date = {julian_date:0.12f}")

