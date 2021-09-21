'''
A program that calculates the average student height from a List of heights.
Using For loop. Not using len() and sum()
'''

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

n = 0
for n in range(0, len(student_heights)):
    total = n+1
print (f"Total students = {total}")

sum = 0
for y in student_heights:
    sum += y

avg = round(sum / total) 
print(f"average height of student = {avg}")