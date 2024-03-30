# a program to calculate remaining life in weeks left

age = int(input("Enter your age:\n"))

#let's say we live for 90 years
max_life_span = 90

#remaining age in years

remaining_age = max_life_span - age

#remaining age in weeks 
weeks_left = remaining_age * 52 # 52 weeks in a year

print(weeks_left)