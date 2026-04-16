#A simple program that asks user to enter their grade and
#calculates the final grade usinf a while loop
# Author: Kaweny Ezidio

#create variables to store data
final_grade: 0

#ask user to enter input
m = int(input("How many assignments did you complete? "))
#make a copy of the number of assignments
n = m
#declare variable to sum all grades
grades_sum = 0
#create a while loop so user can enter all grades
while n!= 0:
	grade =float(input("Enter grade: "))
	grades_sum = grades_sum + grade #sum all grades
	n=n-1 #count down the number of iterations
#calculate final grade and display it
final_grade = grades_sum/m
print("Your final grade is :",final_grade)
