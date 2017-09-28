#!/usr/bin/env python3

hourly = float(input("Please enter the normal hourly wage: ")) # grab the hourly pay
regular = float(input("Enter the number of regular hours: ")) # get the number of regular hours
overtime = float(input("Enter the number of overtime hours ")) # get the number of overtime hours
overtime_wage = (hourly * 1.5) # get the wage of overtime (based on hourly wage)
weekly = float((hourly * regular) + (overtime * overtime_wage)) # get the total wages for the week
print("The final pay for this week is",weekly) # print it!
