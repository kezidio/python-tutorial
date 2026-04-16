#A simple program that asks user to enter their grade and
#calculates the final grade usinf a while loop
# Author: Kaweny Ezidio


final_grade: 0
m = int(input("How many assignments did you complete? "))
n = m
grades_sum = 0
while n!= 0:
	grade =float(input("Enter grade: "))
	grades_sum = grades_sum + grade
	n=n-1

final_grade = grades_sum/m
print("Your final grade is :",final_grade)
