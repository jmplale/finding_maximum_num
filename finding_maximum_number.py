# we need to make inputs for the user.

num_one = int(input("What is your first number?: "))
num_two = int(input("What is your second number?: "))
num_three = int(input("What is your third number?: "))

# we need to make if statement for num_one
if num_one > num_two and num_one > num_three:
    print("\nThe largest number among the three numbers you've entered is " + str(num_one))

# also an if statement for num_two 
if num_two > num_one and num_two > num_three:
    print(print("\nThe largest number among the three numbers you've entered is " + str(num_two)))
    
# the else statement for num_three