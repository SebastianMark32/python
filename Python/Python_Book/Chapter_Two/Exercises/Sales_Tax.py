# Sales tax

# Taking user input
purchase_amount = float(input("Enter the purchaser amount:"))

# State tax
state_tax = 0.05

# County tax 
county_tax = 0.025

# Total for county and state
total_state_tax = purchase_amount * state_tax

# Total for county tax
total_county_tax = purchase_amount * county_tax

# Displaying to the console for state and county tax
print("Purchase amount:", purchase_amount)
print("State sales tax:", total_state_tax)
print("County sales tax:", total_county_tax)
print("Total sale:", purchase_amount + total_county_tax + total_state_tax)
