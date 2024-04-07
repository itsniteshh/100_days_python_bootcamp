#from art import logo

#print(logo)


def add(n1, n2):
    total = num1 + num2
    return total

def subtract(n1, n2):
    total = num1 - num2
    return total

def multiply(n1, n2):
    total = num1 * num2
    return total

def division(n1, n2):
    total = num1 / num2
    return total

end_of_game = True
num1 = int(input("Enter number: "))


while end_of_game:
    num2 = int(input("Enter another number: "))
    operator = input("pick an operation:\n+\n-\n*\n/\n")
    
    if operator == "+":
        total = add(num1, num2)
    elif operator == "-":
        total = subtract(num1, num2)
    elif operator == "*":
        total = multiply(num1, num2)
    elif operator == "/":
        total = division(num1, num2)
    else:
        print("Wrong input")
    
    print(f"The total is {total}")
    
    
    another_game = input("Type no to quit: ").lower()
    
    if another_game == "yes":
        num1 = total
    else:
        end_of_game = False