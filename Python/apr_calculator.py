#!/usr/bin/env python3

deposit = float(input("What is the amount you will be depositing?\n")) # get the amount to be deposited
apr = float(input("Please enter the APR for the account. For example (2) will be read as 2% or 0.02\n")) # get the percent APR
years = int(input("How many years will it gain interest?\n")) # get the number of years
interest = ((apr / 100) + 1) # calculate the interest. Will always be 1.XX unless interest is over 100%
total = (interest** years) * deposit # calculate the final amount in the account
final = round(total, 2)
print("Your final amount will be: $",final) # print the amount to the console
