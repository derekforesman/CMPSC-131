#!/usr/bin/env python3

student_1 = input("Enter the first student's name:\t") # get the first student's name
score_1 = float(input("Enter their score:\t")) # get the first student's score
student_2 = input("Enter the second student's name:\t") # get the second student's name
score_2 = float(input("Enter their score:\t")) # get the second student's score

print("Name:","\t\t","Score:") # start the table
print(student_1, "\t\t", score_1) # add the first student and their score
print(student_2, "\t\t", score_2) # add the second student and their score
average = (score_1 + score_2) / 2 # average the two scores
final = round(average,1) # round them to the first point
print("The average score between them is",final) # print the final score
