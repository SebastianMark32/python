# Comparing characters using ASCII values

# User input
first_letter = input("Enter a letter:")
second_letter = input("Enter the second letter:")

# Comparing the two characters
if first_letter < second_letter:
    print("The first letter is smaller than the second letter by ASCII value!")
elif first_letter == second_letter:
    print("Both characters are the same")
else:
    print("The second letter is greater than the first letter by ASCII value!")