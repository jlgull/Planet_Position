#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work on calculating prime numbers and also timing them to the second.
#   To time to nSeconds, switch which of the perf_counter items to use,
#   and also change the format and label in the print statmets.
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

#
# End of the Import section.
#


#
# Define functions
#


# Set the while control value to "Y".
do_again = "Y"

# Use while, regarding the desire to re-run the program.
while do_again != "N":

    # Establish base variables.
    prime_numbers = list()
    prime_numbers.append(1)
    prime_numbers.append(2)
    counter = 0

    # Main body of the program.

    clear()

    print(f"\nThis program will find all the prime numbers between the two (2) numbers you enter.")

    lower_limit = get_data("i", "Enter your lower limiting integer now: ")
    upper_limit = get_data("i", "Enter your upper limiting integer now: ")

    tic = perf_counter()

    if lower_limit < 3:
        print(2, end=", ")
        counter = 1

    # Code to actually find the prime numbers and print them out.
    for outside_loop in range(3, upper_limit+1, 2):
        for inside_loop in range(3, outside_loop+1, 2):
            if outside_loop % inside_loop == 0 and inside_loop in prime_numbers:
                break
            if outside_loop % inside_loop == 0 and outside_loop not in prime_numbers:
                prime_numbers.append(outside_loop)
                if outside_loop >= lower_limit:
                    print(outside_loop, end=", ")
                    counter += 1

    toc = perf_counter()
    print(f"\nRun time is {toc - tic:0.4f} seconds")

    print(f"Between {lower_limit} and {upper_limit} there were {counter} Prime numbers.")

    # Ask if the user would like to repeat the program.
    # Also, validate for the correct response.
    while True:
        print("\nWould you like to run this again? Enter (Y) for yes or (N) for no.", end=" ")
        do_again = input().upper()
        if do_again == "N" or do_again == "Y":
            break
        else:
            print("The only valid entries are either a Y or an N.")

# End of Program
