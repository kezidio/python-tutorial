#This program demonstrates how to convert a temperature from Fahrenheit
#to Celsius using a mathematical formula. It shows how user input or 
#variable values can be processed to produce a converted result.

#declare a variable and ask user to enter the temperature in F to be converted
tempF = input("Enter temperature in F:")
 
#declare variable and calculate temperature  conversion to celsius
tempC= (float(tempF)-32)*5/9

#display temperature in C
print("The tempture in C is", tempC)


