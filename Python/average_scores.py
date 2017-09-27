#!/usr/bin/env python3

student_1 = input("Enter the first student's name:\t") # get the first students name
score_1 = float(input("Enter their score:\t"))# get their score
student_2 = input("Enter the second student's name:\t")# get the second students name
score_2 = float(input("Enter their score:\t"))# get their score

print("Name","\t\t","Score")# make the table (\t is annoying)
print(student_1, "\t\t", score_1)# print to the table
print(student_2, "\t\t", score_2)# print to the table
average_score = (score_1 + score_2) / 2# add the scores
average = round(average_score,1)# round to the first number after the decimal point
print("The average score for both students is: %s." %(average))# print the average score
