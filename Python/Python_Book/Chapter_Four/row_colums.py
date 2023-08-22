# Taking user input to detemine how many rows and colums of *

# Taking user input
rows = int(input("How many rows would you like?:"))
columns = int(input("How many colums would you like?:"))

# Nested loop to build rows and colums
for r in range(rows):
    for c in range(columns):
        print("*", end='')
    print()