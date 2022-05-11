#!/usr/bin/env python3
#
# Author: Jonathan Heard
# Work on learning how to import and manipulate CVS data in Pyton.
#   The starting point for this learning is https://www.educba.com/python-import-csv/.
#
#
# Import all required items.
#


import csv


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

#
# End of the Import section.
#

# Main body of test program
print("Program to demonstrate csv.reader() function:")
print("\n")

celestial_csv_data = "Celestial_Objects.csv"
"""
# c = open(celestial_csv_data, 'r')
solar_data = with open(celestial_csv_data)
print("The csv file is opened for reading:")
print("\n")

o = csv.reader(solar_data)
print("The contents of the above file is as follows:")
for r in o:
    print(r)
c.close()
"""
with open(celestial_csv_data) as solar_data:
    solar_data_dic = csv.DictReader(solar_data)
    print(type(solar_data_dic))
    print("\n")
    for row in solar_data_dic:
        print(row)
        """
        print(row['Object Name'], row['N-fixed'], row['N-daily'], row['i-fixed'], row['i-daily'],
              row['w-fixed'], row['w-daily'], row['a'], row['e-fixed'], row['e-daily'], row['M-fixed'],
              row['M-daily'])
        """

# End of program
