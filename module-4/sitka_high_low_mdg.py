# Mike Gordon
# CSD325 Advanced Python 
# 9/1/26

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'module-4/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)



# Function to display the high temperatures
def show_highs():
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Function to display the low temperatures
def show_lows():

    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

while True:
    print('\nThis is the Sitka Weather Program.')
    print('\nPlease select an option (1 for highs, 2 for lows, or 3 to quit the program.)')

    # Loop until valid user input
    while True:

        user_input = input('\nType your selection: ')

        if user_input == '1':
            show_highs()
            break
        elif user_input == '2':
            show_lows()
            break
        elif user_input == '3':
            print('\nThank you for using the program. Goodbye.\n')
            sys.exit()
        else:
            print('\nThat was not a valid selection. Please type 1, 2, or 3.')