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

class Object:
    """
    Define the Object class, as each record is created the necessary data is collected.

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

    One Astronomical Unit (AU) is the Earth's mean distance to the Sun, or 149.6 million km. When closest to the
        Sun, a planet is in perihelion, and when most distant from the Sun it's in aphelion. For the Moon,
        an artificial satellite, or any other body orbiting the Earth, one says perigee and apogee instead,
        for the points in orbit least and most distant from Earth.

    """
    def __init__(self):
        # Celestial objects identifier
        self.object_name = get_data("s", "Enter the Celestial Objects name: ")
        # N = longitude of the ascending node, float
        self.N_fixed = get_data("f", "Enter (N), fixed data for the longitude of the ascending node: ")
        self.N_daily = get_data("f", "Enter (N), daily data for the longitude of the ascending node: ")
        # i = inclination to the ecliptic (plane of the Earth's orbit), float
        self.i_fixed = get_data("f", "Enter (i), fixed data for the inclination to the ecliptic: ")
        self.i_daily = get_data("f", "Enter (i), daily data for the inclination to the ecliptic: ")
        # w = argument of perihelion, float
        self.w_fixed = get_data("f", "Enter (w), fixed data for the argument of perihelion: ")
        self.w_daily = get_data("f", "Enter (w), daily data for the argument of perihelion: ")
        # a = semi-major axis, or mean distance from Sun, float
        self.a = get_data("f", "Enter (a), the semi-major axis, in AU: ")
        # e = eccentricity (0=circle, 0-1=ellipse, 1=parabola), float
        self.e_fixed = get_data("f", "Enter (e), fixed data the eccentricity: ")
        self.e_daily = get_data("f", "Enter (e), daily data the eccentricity: ")
        # M = mean anomaly (0 at perihelion; increases uniformly with time)
        self.M_fixed = get_data("f", "Enter (M), fixed data the mean anomaly: ")
        self.M_daily = get_data("f", "Enter (M), daily data the mean anomaly: ")

    def info_planet(self):
        print(
            f"For object named {self.object_name.title()}:\n"
            f"\tthe N values are:   {self.N_fixed} and {self.N_daily}\n"
            f"\tthe i values are:   {self.i_fixed} and {self.i_daily}\n"
            f"\tthe w values are:   {self.w_fixed} and {self.w_daily}\n"
            f"\tthe a value is:     {self.a}\n"
            f"\tthe e values are    {self.e_fixed} and {self.e_daily}\n"
            f"\tthe M values are    {self.M_fixed} and {self.M_daily}\n"
            )






if __name__ == "__main__":

    planet = list()

    clear()
    print()

    planet.append(Object())

    for p in planet:

        print(p.info_planet())



"""

Orbital elements of the Sun:
    N = 0.0
    i = 0.0
    w = 282.9404 + 4.70935E-5 * d
    a = 1.000000  (AU)
    e = 0.016709 - 1.151E-9 * d
    M = 356.0470 + 0.9856002585 * d
Orbital elements of the Moon:
    N = 125.1228 - 0.0529538083 * d
    i = 5.1454
    w = 318.0634 + 0.1643573223 * d
    a = 60.2666  (Earth radii) or 0.0025695 (AU)
    e = 0.054900
    M = 115.3654 + 13.0649929509 * d
Orbital elements of Mercury:
    N =  48.3313 + 3.24587E-5 * d
    i = 7.0047 + 5.00E-8 * d
    w =  29.1241 + 1.01444E-5 * d
    a = 0.387098  (AU)
    e = 0.205635 + 5.59E-10 * d
    M = 168.6562 + 4.0923344368 * d
Orbital elements of Venus:
    N =  76.6799 + 2.46590E-5 * d
    i = 3.3946 + 2.75E-8 * d
    w =  54.8910 + 1.38374E-5 * d
    a = 0.723330  (AU)
    e = 0.006773 - 1.302E-9 * d
    M =  48.0052 + 1.6021302244 * d
Orbital elements of Mars:
    N =  49.5574 + 2.11081E-5 * d
    i = 1.8497 - 1.78E-8 * d
    w = 286.5016 + 2.92961E-5 * d
    a = 1.523688  (AU)
    e = 0.093405 + 2.516E-9 * d
    M =  18.6021 + 0.5240207766 * d
Orbital elements of Jupiter:
    N = 100.4542 + 2.76854E-5 * d
    i = 1.3030 - 1.557E-7 * d
    w = 273.8777 + 1.64505E-5 * d
    a = 5.20256  (AU)
    e = 0.048498 + 4.469E-9 * d
    M =  19.8950 + 0.0830853001 * d
Orbital elements of Saturn:
    N = 113.6634 + 2.38980E-5 * d
    i = 2.4886 - 1.081E-7 * d
    w = 339.3939 + 2.97661E-5 * d
    a = 9.55475  (AU)
    e = 0.055546 - 9.499E-9 * d
    M = 316.9670 + 0.0334442282 * d
Orbital elements of Uranus:
    N =  74.0005 + 1.3978E-5 * d
    i = 0.7733 + 1.9E-8 * d
    w =  96.6612 + 3.0565E-5 * d
    a = 19.18171 - 1.55E-8 * d  (AU)
    e = 0.047318 + 7.45E-9 * d
    M = 142.5905 + 0.011725806 * d
Orbital elements of Neptune:
    N = 131.7806 + 3.0173E-5 * d
    i = 1.7700 - 2.55E-7 * d
    w = 272.8461 - 6.027E-6 * d
    a = 30.05826 + 3.313E-8 * d  (AU)
    e = 0.008606 + 2.15E-9 * d
    M = 260.2471 + 0.005995147 * d
"""