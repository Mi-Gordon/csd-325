# Mike Gordon
# CSD325 Advanced Python
# Module 2.2 Assignment
# 8/17/2026

# Program from Previous Python Course

def main ():
    greeting()

        # Get number of feet of fiber to be installed
    while True:
        try:
            feet_to_install = float(input('How many feet must be installed? '))
            if feet_to_install > 0:
                break
            else:
                print('Must be greater than zero.')
        except ValueError as e:
            print(e)

    calculate(feet_to_install)



def greeting():

    # Welcome message
    greeting = 'Welcome to Fiber & More!'
    print()  # Add a space before the welcome
    print(f'*****{greeting:^50}*****')
    print()  # Add a space after the welcome
    print('This program is used to calculate the cost to install fiber optic cable.\n')

def calculate(feet_to_install):
    # Multipy number of feet times .87
    # Convert user input to a float for calculation
    length = feet_to_install
    COST = .87  # Named Constant

    total_cost = length * COST  # Calculate total cost

    # Display the calculated information and company name
    # f string is used to utilize variables and .2f reduces calculation to two decimals
    print(
        f'\n\nThe total cost to install {feet_to_install} feet of fiber optic cable is ${total_cost:.2f}.\n')
    print('Thank you for choosing Fiber & More, have a great day!\n')


if __name__ == "__main__":
    main()

