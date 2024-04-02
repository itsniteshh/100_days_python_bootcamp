# a program to get avg height of all students based on the input


user_height = input("Enter your height followed by commas:\n").split(",")

for n in range(len(user_height)):
    user_height[n] = int(user_height[n])
    
total_height = 0
count_students = 0

for nums in user_height:
    total_height += nums
    count_students += 1

avg_height = total_height / count_students

print(f"The average height of your group is {round(avg_height, 2)}")