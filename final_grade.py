#A simple program that asks user to enter their grade and
#calculates the final grade usinf a while loop
# Author: Kaweny Ezidio


final_grade:0
n=0
m = int(input("How many assignments did you complete? "))
m = n
while n!= 0:
	grade =float(input("Enter grade: "))
	final_grade = final_grade + grade
	n-1

final_grade=final_grade/m
print("Your final grade is :",final_grade)

