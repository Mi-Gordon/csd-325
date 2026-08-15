# Mike Gordon
# CSD325 Module 1
# 8/14/26

def main():

    # Start with running the greeting function
    greeting()

    # Get user input and validate it
    while True:
        # Ensure user input is a number and greater than zero
        try:
            num_bottles = int(input("Enter number of bottles: "))

            if num_bottles > 0:
                break
            else:
                print('This must be a number greater than zero.')

        # Throw value error if not a number
        except ValueError:
            print('This must be a number!')

    # Pass user input to countdown function
    countdown(num_bottles)

    # Print final message before the program terminates
    print('\nTime to buy more bottles of beer.\n')


def countdown(num_bottles):

    # Start the loop counting down the number of bottles
    while num_bottles > 0:

        if num_bottles > 1:

            # Set a variable to hold new value for the message
            new_num = num_bottles - 1
            print(
                f'\n{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.')
            print(
                f'Take one down and pass it around, {new_num} bottle(s) of beer on the wall.')

            # Decrease the number of bottles each itteration
            num_bottles -= 1

        # Change message once count get to one
        elif num_bottles == 1:
            print(
                f'\n{num_bottles} bottle of beer on the wall, {num_bottles} bottle of beer.')
            print(f'Take one down and pass it around, 0 bottles of beer on the wall.')

            # Still need to decrease to prevent endless loop
            num_bottles -= 1


# Welcome the user and give an explination of what the program does
def greeting():
    print('\nWelcome to the "Bottles of Beer" program. Please enter a number of bottles to start with.')
    print('The program will count down to zero from there!\n')


if __name__ == '__main__':
    main()
