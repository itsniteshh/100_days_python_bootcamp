# a program to check odd and even numbers

number = int(input("Enter a number:\n"))

if number % 2 == 0:
    print(f"{number} = even")
else:
    print(f"{number} = odd")