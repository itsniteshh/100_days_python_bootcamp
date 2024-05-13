# a program to check if a year is a leap year or not provided prerequites


year = int(input("Enter a year:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("Leap year")
    
else:
    print("Not leap year")