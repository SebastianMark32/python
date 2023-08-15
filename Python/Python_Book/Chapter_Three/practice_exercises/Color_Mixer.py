# Color mixer
# this program will check the resulting color when 
# two primary colors are mixed together
'''
Primary colors are: Red, Blue and Yellow
because they cannot be made by mixing other colors. 
Also if we mix two primary colors we get a secondary color
 '''

# Taking user input for two primary colors 
primary_one = input("Enter the first primary color (red, blue or yellow): ")
primary_two = input("Enter the second primary color: ")

# Checking permutations of red, blue and yellow color mix
if primary_one == "red" and primary_two == "blue":
    print("Red and blue make purple!")
elif primary_one == "red" and primary_two == "yellow":
    print("Red and yellow make orange!")
elif primary_one == "blue" and primary_two == "yellow":
    print("Blue and yellow make green!")
else:
    print("Invalid input, must enter primary colors e.g., red, blue or yellow.")






