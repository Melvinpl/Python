student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] >= 91:
        grade = "Outstanding"
    elif student_scores[key] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        grade = "Acceptable"
    elif student_scores[key] <= 70:
        grade = "Fail"
    student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)