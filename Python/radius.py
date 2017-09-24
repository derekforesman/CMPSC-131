#!/usr/bin/env python3

from math import sqrt, pi # import sqrt and pi as the whole math module is not needed

area = float(input("Please enter the area of the circle: ")) # grab the area as a float
radius = float(sqrt(area / pi)) # get the radius by dividing by pi and taking the square root
print("The radius of the circle is", radius) # print the final radius
