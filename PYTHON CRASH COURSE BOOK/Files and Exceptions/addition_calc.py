


while True:
    num1 = int(input("Enter any number: "))
    num2 = input("Enter another number: ")
    
    if num2 == "q":
        break


    try:
        print(num1 + int(num2))
        
    except:
        pass
    