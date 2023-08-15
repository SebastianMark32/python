# Average test and conditionals

 # Taking user input to calculate the test scores
test1 = int(input("Enter first test score:"))
test2 = int(input("Enter second test score:"))
test3 = int(input("Enter third test score:"))
test4 = int(input("Enter fourth test score:"))

# Calcuating the average test score
average = (test1 + test2 + test3 + test4) / 4

# Conditional for passing the course
if average < 70:
    print("I am sorry but you did not pass the class! Your score is", average)
elif average == 70:
    print("Your scorer:", average)
    print("You just passes the classes with the minimun score")
elif average >= 95:
    print("Congratulations! You did so well in the class with an average score of:", average)
else:
    print("Your score:", average)
    print("You passed the course! Congrats!")