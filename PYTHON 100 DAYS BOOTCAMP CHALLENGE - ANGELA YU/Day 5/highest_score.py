student_score = [50, 100, 520, 42, 53, 53, 55, 66, 2800]

highest_score = 0

for score in student_score:
    if score > highest_score:
        highest_score = score
        
print(f"The highest score is {highest_score}")

total = 0
for num in range(101):
    total += num
print(total)