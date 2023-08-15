# Mass and weight 
# Newtons weight formula, weight = mass * 9.8

# Taking objects mass user input
mass = int(input("Enter the objects mass: "))

# Using formula to caculate mass into Newtons
newtons = mass * 9.8

# Checking mass condition weight restrictions
if newtons > 500: 
    print("Too heavy, the mass has exceesing weight")
elif newtons < 100:
    print("Too light, need more mass")
else:
    print("The current newtons:", format(newtons, '.2f'))
