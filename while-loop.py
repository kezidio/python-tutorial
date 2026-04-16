#This program demonstrates the use of a while loop to repeatedly execute a
#block of code as long as a condition remains true. It shows how loops 
#can automate repetitive tasks and control the flow of a program.

#display prompt
print("Enter a sequence of numbers to be added. The program will stop once you enter the number 0")

#declare variable to store the results
result= 0

#declare variable to store values entered by user
number_to_be_added = 1

 #while used enter number different than zero
while valor != 0:
	#ask user for a number
	number_to_be_added = int(input("Enter number:"))
	#calculate the sum 
	result= result+number_to_be_added
	
	#display results
print("The total is:", result)

