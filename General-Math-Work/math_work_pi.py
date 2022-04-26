#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work for CIS156, based on zyBook, CIS156: Python Programming: Level 1
# copied out of Chapter 5.9 to practice and change.
#

#
# Import all required options
#
from kennedy_13 import clear

from math import pi, pow

#
# Define functions
#

# Start of program

clear()

# Read file

print()

pi2 = 355 / 113

pi_delta = ((pi2 / pi) - 1) * pow(10, 9)


print(f"Pi from math module:       {pi}")
print(f"Pi2 from local (355/113):  {pi2}")
print(f"Pi2/Pi error in ppb:      {pi_delta}")

# End of program
