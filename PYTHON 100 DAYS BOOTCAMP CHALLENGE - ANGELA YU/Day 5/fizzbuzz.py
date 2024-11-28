for nums in range(1, 101):
    if nums % 15 == 0:
        print(f"{nums} - fizzbuzz")
    elif nums % 3 == 0:
        print(f"{nums} - Fizz")
    elif nums % 5 == 0:
        print(f"{nums} - Buzz")
    else:
        print(nums)