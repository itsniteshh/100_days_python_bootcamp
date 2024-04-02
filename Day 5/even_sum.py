# summing all the even numbers between 1 to x (user input)

nums = int(input("Enter number:\n"))

   
total = 0
#nums = [10, 12, 13, 15]

for numbers in range(nums):
    if numbers % 2 == 0:
        total += numbers
    else:
        pass

print(f"The total sum of even numbers is {total}")