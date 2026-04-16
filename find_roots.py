#This program demonstrates how to solve a quadratic equation using the quadratic formula.
#It uses if statements to handle different cases based on the discriminant and float 
#values to ensure accurate calculations. The program helps find the real roots. 


import math

#declare variables and ask user to insert numbers
a=float(input("a "))
b=float(input("b "))
c=float(input("c "))

#calculate how many real solutions the equation has (b² − 4ac)
D = b** 2 -4 * a * c

#if D = 0, the equation has one real solution (repeated root)
if(D ==0):
        root_1=(-b+math.sqrt(D))/(2 * a)
        print("The root is",root_1) #display root if this case is true
              

else:
#else, check if D < 0, if true, the equation has no real solutions (two complex roots)
    if(D<0):
        print("There is no real root") #display message if this case is true
        
    #if previous conditions are false, there two real solutions and they will be displayed in this last statement
    else:
        root_1=(-b+math.sqrt(D))/(2 * a)
        root_2=(-b-math.sqrt(D))/(2 * a)
        if(root_1<root_2):
                print("The roots are ",root_1," and ",root_2)
        else:
                print("The roots are ",root_2," and ",root_1)
        
