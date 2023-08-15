# Comparing two rectangles

# Taking user input for the first rectangle
length_1 = int(input("Enter the length for rectangle 1: "))
width_1 = int(input("Enter the width foe rectangle 1: "))

# Taking user input for the second rectangle
length_2 = int(input("Enter the length for the second rectangle: "))
width_2 = int(input("Enter the width for the second rectangle: "))

# Area
recatangle_1 = length_1 * width_1
rectangle_2 = length_2 * width_2

# Comparing the area of both rectangles
if recatangle_1 > rectangle_2:
    print("Rectangle 1 has a greater area")
elif recatangle_1 < rectangle_2:
    print("Rectangle 2 has a greater area")
else:
    print("Both rectangles have the same area")