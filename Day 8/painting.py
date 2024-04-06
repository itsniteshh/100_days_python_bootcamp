# A program to calculate the count the number of cans required to paint 
import math

height = int(input("Enter height of the wall:\n")) 
width = int(input("Enter width of the wall:\n"))

coverage_per_can = 5

def paint_calc(h, w, cover):
    
    test = (height * width) / coverage_per_can
    
    #rounding the value and returning it for the end user
    return print(f"You will need {math.ceil(test)} cans of paint.")
    
paint_calc(h = height, w = width, cover = coverage_per_can )