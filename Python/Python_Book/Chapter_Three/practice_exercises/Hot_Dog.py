# This program check for how many hot dogs and buns are 
# needed for a cookout. Assume each package of 
# hot dogs come in 10 and buns come in 8 

# Constant variables
hot_dog_pack = 10
buns_pack = 8

# User input for how many antendee's
total_people = int(input("How many people are coming to the cookout?: "))

# User input for person-per-hot-dog ratio
hot_dog_per_person = int(input("How many hot dogs will each person eat?: "))

# Calculating person-per-hot-dog
total_hot_dogs = total_people * hot_dog_per_person

# Total packs of hot dogs neeeded per event
total_hot_dog_packs = total_hot_dogs / hot_dog_pack
print("Minumum number of hot dog packs required:", total_hot_dog_packs)

# Total pack of buns needed per event
total_buns_pack = total_hot_dogs / buns_pack
print("Minumum number of bun packs required:", total_buns_pack)

# Leftover buns calcuation
remainder = (total_hot_dog_packs * 2) % buns_pack
print("Leftover buns:", remainder)
