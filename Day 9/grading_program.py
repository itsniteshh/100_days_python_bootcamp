student_score = {
    "Harry": 81,
    "Ron": 53,
    "Nitesh": 56,
    "Arjun": 68
}


#creating an empty dictionary called stud_grades
student_grades = {}

for student in student_score:
    score = student_score[student]

if score > 90:
    student_grades[student] = "Outstanding" 
elif score > 80:
    student_grades[student] = "Exceeds Expectations" 
elif score > 70:
    student_grades[student] = "Acceptable"
else:
    student_grades[student] = "Fail"

print(student_grades)