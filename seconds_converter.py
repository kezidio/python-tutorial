#This program demonstrates how to convert a given number of seconds into 
#days, hours, minutes, and seconds. It shows how mathematical operations 
#can be used to break down a single value into more meaningful time units.

#declare variable and ask user to enter a number
seconds_total=int(input("Please enter the number of seconds to be converted:"))
#seconds_int=int(segundos)

#calculate the days
days=(seconds_total//86400)

#calculate the remaining
remaining=seconds_total%86400

#calculate the hours
hours=remaining//3600

#calculate the minutes
still_remaining=remaining%3600
minutes =still_remaining//60

#calculate what is left
seconds_remaining=still_remaining%60

#display results
print(days," days, ",hours," hours, ", minutes, " minutes, ", " and ",seconds_remaining, " seconds.")
