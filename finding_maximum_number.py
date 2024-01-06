# let us put design in our code
# we will import some tools that will help us to design the result of our code
from pyfiglet import Figlet
import colorama

# we will just set up some definition that we can use in designing the code

colorama.init()

def for_print(text, color):
    print(color + text + colorama.Style.RESET_ALL)
def colored_letter(text, color):
    return color + text + colorama.Style.RESET_ALL    
    

# we need to make inputs for the user.

def main():  # putting def main to put some design to the code
    num_one = int(input("What is your first number?: "))
    num_two = int(input("What is your second number?: "))
    num_three = int(input("What is your third number?: "))
   
    # I just fixed some few errors
    # we need to make if statement for num_one
    if num_one > num_two and num_one > num_three:
        print("\nThe largest number among the three numbers you've entered is " + str(num_one))
    else:
        # also an if statement for num_two 
        if num_two > num_one and num_two > num_three:
            print(("\nThe largest number among the three numbers you've entered is " + str(num_two)))

        # the else statement for num_three
        else:
            print(("\nThe largest number among the three numbers you've entered is " + str(num_three)))

            