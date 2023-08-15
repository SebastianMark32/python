# Calculating the total distance traveled 
# Distance formula is distance = speed * time

# Taking user input for speed
speed = int(input("Enter your current rate in MPH:"))

# Taking user input for time taken to destination
time = float(input("Enter your ETA in hours:"))

# Applying the distance formula 
distance = speed*time

# Display the current rate to the console truncating to two decimal places
print("Total distance traveled:", format(distance, '.2f'))