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

    # let's add some font design
    font = Figlet(font = 'small')
    another_font = Figlet(font = 'mini')

    # making introduction on the outcome
    introduction = colored_letter(font.renderText("Welcome to the Maximum Number Finder Machine!"), colorama.Fore.MAGENTA)
    for_print(introduction, colorama.Fore.MAGENTA)

    num_one = int(input("What is your first number?: "))
    num_two = int(input("What is your second number?: "))
    num_three = int(input("What is your third number?: "))
   
    # I just fixed some few errors
    # we need to make if statement for num_one
    if num_one > num_two and num_one > num_three:
        for_print(colored_letter(another_font.renderText("\nThe largest number among the three numbers you've entered is " + str(num_one)), colorama.Fore.BLUE), colorama.Fore.BLUE)
    else:
        # also an if statement for num_two 
        if num_two > num_one and num_two > num_three:
            for_print(colored_letter(another_font.renderText("\nThe largest number among the three numbers you've entered is " + str(num_two)), colorama.Fore.GREEN), colorama.Fore.GREEN)

        # the else statement for num_three
        else:
            for_print(colored_letter(another_font.renderText("\nThe largest number among the three numbers you've entered is " + str(num_three)), colorama.Fore.YELLOW), colorama.Fore.YELLOW)

if __name__ == "__main__":
    main()
