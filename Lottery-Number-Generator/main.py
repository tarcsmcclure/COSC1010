#
# Anna McClure
# 4/14/25
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
import random

MAX_DIGITS = 7 #Max number of digits 
START = 0  # start of the random number range
END = 9  # End of the random number range

#calling the main function
def main():
    #create the list
    numbers = [0] * 7

    #populate the list with random numbers
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    #Display the random numbers
    print('Here are your lottery numbers:')
    for index in range(MAX_DIGITS):
        print(numbers[index], end='')
    print()

#Call the main function
main()