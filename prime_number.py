# A simple program that checks whether a given number is 
# prime or not by testing its divisibility.
# Author: Kaweny Ezidio

#declare variable and ask user to enter number
number=int(input("Please enter a whole number: "))

#declare a variable to check if number is even
div=2

#declare a variable and assign value true
prime=True

#create a while loop to check all cases
#while 2 <= num-1 and true
while(div<=number-1) and (prime):
        #if number remainder of 2 = 0
        if(number%div==0):
                prime= False
         #add 1 to check remainder       
        div=div+1
        
if(prime and not number==1):
        print("Prime number!")
else:
        print("Not a prime number!")
        

        
        
        
