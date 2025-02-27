#
# Anna McClure
# 2/27/25
# Budget Analysis Programming Project
# COSC 1010
#initialize the variables
budget = 0
bills = 0
total_bills = 0
amt_left = 0

#Set the inputs to get the total budget and the amount of the 1st bill to start the loop.
budget = float(input('Enter your budget for the month in dollars $'))
bills = float(input('Enter the amount of the bill, enter 0 to end. $'))

#Start the while loop, while the bills isn't 0 which would end the loop the user will keep getting prompted.
while bills != 0:
    #This is the prompt until 0 is entered to end the loop
    bills = float(input('Enter the amount of your next bill, enter 0 to end. $'))
#Adds all the bills together to give total bills
    total_bills += bills
#Calculates the amount left in budget
    amt_left = budget - total_bills
#prints the total of the bills and the amount left after paying all bills
print('The total amount of your monthly bills is $',total_bills, 'the amount you will have left after paying bills is $',amt_left)

# Use comments liberally throughout the program. 