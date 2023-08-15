''' Miles-per-gallon Forumula for MPG is MPG = Miles driven / Gallons of gas'''

# Taking user input for the number of miles driven
miles_driven = float(input("How miles did you drive?: "))

# Taking user input for the amount of gallons used
gallons_of_gas = float(input("How many gallons of gas did you use?: "))

# Calculating the formula for MPG
MPG = miles_driven / gallons_of_gas

# Displaying MPG to the console
print("Your current MPG is:", format(MPG, '.2f'))
