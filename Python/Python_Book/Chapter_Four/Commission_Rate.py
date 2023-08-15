# Testing some loop

# Control variable for the while loop
keep_going = 'n'

# Calculating a series of commissions
while keep_going == 'y':
    # Getting the persons total in sales
    sales = float(input("Enter your sales:"))
    commission_rate = float(input("Enter your commission rate:"))

    # Calculating the commission
    commission = sales * commission_rate

    # Displaying the commission rate to the console
    print("THe commission is $", format(commission, '.2f'), sep='')

    # Taking user input for the while loop condition
    keep_going = input("Would you like to keep going? Presss 'y' if so:")