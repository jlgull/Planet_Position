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


from datetime import datetime, date, time


#
# End of the Import section.
#

"""
The primary orbital elements are here denoted as:
    N = longitude of the ascending node
    i = inclination to the ecliptic (plane of the Earth's orbit)
    w = argument of perihelion
    a = semi-major axis, or mean distance from Sun
    e = eccentricity (0=circle, 0-1=ellipse, 1=parabola)
    M = mean anomaly (0 at perihelion; increases uniformly with time)
    
Related orbital elements are:
    w1 = N + w   = longitude of perihelion
    L  = M + w1  = mean longitude
    q  = a*(1-e) = perihelion distance
    Q  = a*(1+e) = aphelion distance
    P  = a ^ 1.5 = orbital period (years if a is in AU, astronomical units)
    T  = Epoch_of_M - (M(deg)/360_deg) / P  = time of perihelion
    v  = true anomaly (angle between position and perihelion)
    E  = eccentric anomaly
    
One Astronomical Unit (AU) is the Earth's mean distance to the Sun, or 149.6 million km. When closest to the Sun, 
    a planet is in perihelion, and when most distant from the Sun it's in aphelion. For the Moon, an artificial
    satellite, or any other body orbiting the Earth, one says perigee and apogee instead, for the points in orbit
    least and most distant from Earth.

"""



clear()
print()

if __name__ == "__main__":


