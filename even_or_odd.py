#This is a simple program that determines whether a given number is odd or even 
#by checking if it is divisible by 2.
#Author: Kaweny Ezidio

#create variable and ask the user for a number
x=int(input("Please enter a whole number: "))
 
#create a variable to check if number is divisible by 2
y=(x%2)

#if remainder is equal to 0 then number is even
if(y==0):
        print("THE NUMBER ", x," is EVEN!")
        
  #else, the number is odd
else:
        print("THE NUMBER ", x,"is ODD!")



