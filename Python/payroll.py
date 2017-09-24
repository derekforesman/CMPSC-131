#!/usr/bin/env python3

hourly = float(input("Please enter the normal hourly wage: "))
regular = float(input("Enter the number of regular hours: "))
overtime = float(input("Enter the number of overtime hours "))
overtime_wage = (hourly * 1.5)
weekly = float((hourly * regular) + (overtime * overtime_wage))
print("The final pay for this week is",weekly)
