#!/usr/bin/env python3

people = int(input("How many people will be going? ")) # grab the number of people going 
car = people % 5 # get the remainder of people divided by the max amount of people in a car

if car == 0: # check to see if people is divisible by 5
    final = int(people / 5) # convert it to an integer
    print("You will need",final,"car(s)") # print the number of cars
elif car >= 1: # check if modulo is greater than 0 
    final = int(people / 5) + 1 # add one to number of cars
    print("You will need",final,"car(s)") # print the number of cars
