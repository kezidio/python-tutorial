#This is a a simple program that uses Python’s 
#built-in random module to generate random numbers, allowing 
#the user to produce unpredictable values for testing, 
#simulations, or basic games.

import random

def main():
    # Get a random number between 1 to 10.
    number = random.randint(1, 10)
    # Display the number.
    print('The number is', number)

# Call the main function.
main()
