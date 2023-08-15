# Special dates is when the month times the day equals the year
# In this program we are going to find some of those magical dates

# User input for the month (numerical)
month = int(input("Enter a month (numerical): "))

# User input for the day
day = int(input("Enter the day in (numerical): "))

# User input for the year
year = int(input("Enter the year (two digits): "))

# Using the formula 
speical_date = month * day

# Checking special date conditions
if year == speical_date:
    print("You have found the special date!")
else:
    print("Keep trying, you did not find the speical date.")