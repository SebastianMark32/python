# Roulette Wheeels are numbered from 0-36
# This program is going to calculate each color per number

# Taking user input for the pocket number
pocket_number = int(input("Enter a pocker number:"))

# Checking all combinations of colors for numbers 0-36
if pocket_number == 0:
    print("Pocket 0 is green")
elif pocket_number >= 1 and pocket_number <= 10:
    if pocket_number % 2 == 0:
        print("Even-numbered pockets are black")
    else:
        print("Odd-numbered pockets are red")
elif pocket_number >= 11 and pocket_number <= 18:
    if pocket_number % 2 == 0:
        print("Even-numbered are red")
    else:
        print("Odd-numbered are black")
elif pocket_number >= 19 and pocket_number <= 28:
    if pocket_number % 2 == 0:
        print("Even-numbered are black")
    else:
        print("Odd-numbered are red")
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number % 2 == 0:
        print("Even-numbered are red")
    else:
        print("Odd numbered are black")
else:
    print("Not a valid range, please try again from 0-36")