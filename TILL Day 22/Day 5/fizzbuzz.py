# fizz buzz program 

for nums in range(100+1):
    if nums % 15 == 0:
        print("Fizzbuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print("Buzz")
    else:
        print(nums)