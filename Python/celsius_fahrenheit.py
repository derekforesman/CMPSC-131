#!/usr/bin/env python3
celsius = float(input("Please enter the degrees in Celsius:\n")) # grab the input in celsius
fahrenheit = (celsius * float((9/5))) + float(32) # convert celsius to fahrenheit with all numbers as floats
final = round(fahrenheit) # round the degrees in fahrenheit to the nearest integer
print(final,"° Fahrenheit",sep='') # print the output to the user
