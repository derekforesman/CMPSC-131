#!/usr/bin/env python3

height = float(input("Please enter your height in inches: ")) # get user's height in inches
weight = float(input("Please enter your weight in pounds: ")) # get user's weight in pounds
meters = (height * 0.0254) # convert user's height to meters
kilos = (weight * 0.454) # convert user's weight to kilograms
finalHeight = (meters ** 2) # get the square of user's height
BMI = round((kilos / finalHeight),1) # get final BMI round to 1 digit after decimal point
print("Your BMI is", BMI) # tell the user their BMI