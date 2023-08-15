# Total Purchase which takes 5 user inputs and caluculates total with 
# 7 percent sales tax

# First item price
item_1 = float(input("Enter the first item price:"))

# Second item price
item_2 = float(input("Enter the second item price:"))

# Third item price
item_3 = float(input("Enter the third itme price:"))

# Fourth item price
item_4 = float(input("Enter the fourth item price:"))

# Fifth item price
item_5 = float(input("Enter the fifth item price:"))

# Subtotal before sales tax
subtotal = item_1 + item_2 + item_3 + item_4 + item_5

# Sales tax at 7%
sales_tax = 0.07

# Total price
tax_amount = subtotal * sales_tax

#Total amount 
total = subtotal + tax_amount

# Display to console
print("Subtotal:", format(subtotal, '.2f'))
print("Sales tax:", sales_tax)
print("Tax:", format(tax_amount, '.2f'))
print("Total with 7% sales tax your total is:",  format(total, '.2f'))


