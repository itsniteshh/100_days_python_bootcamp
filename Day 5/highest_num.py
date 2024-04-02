# program to calculat the highest score from a list of scores

student_score = input("Enter numbers separated by space\n").split(" ")


for num in range(len(student_score)):
    student_score[num] = int(student_score[num])


highest_socre = 0

for nums in student_score:
    if nums > highest_socre:
        highest_socre = nums
        
print(f"The highest number in the list is {highest_socre}")