# This program is to demonstrate the funtionality of for loop and nested loops
# Output will be a triangle pattern with astreks


# Hard capping the size of the triagle
BASE_SIZE = 8

# Base size will be the height of the triangle 
for r in range(BASE_SIZE):
    # Width
    for c in range(r + 1):
        print('*', end='')
    print()
    