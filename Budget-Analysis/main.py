# Anna McClure
# 2/27/25
# Budget Analysis Programming Project
# COSC 1010
#initialize the variables
budget = 0
bills = 0
total_bills = 0
amt_left = 0
#Ask user for monthly budget
budget = float(input('Enter your budget for the month in dollars $'))
#Ask for the first bill
bills = float(input('Enter the amount of the bill, enter 0 to end. $'))
#This loops until the user enters a 0, indicating no more bills
while bills != 0:
    total_bills += bills #this adds the bills up
    amt_left = budget - total_bills # this calculates the amount of money left after paying bills
    #IF statement to check if the bills exceed the budget
    if total_bills > budget:
        print('You do not have enough money to pay your bills')
        break #the break makes it so it stops prompting for bills if you do not have enough moneey
    #This prompts for the next bill, which indicates the user has enough money to continue
    bills = float(input('Enter the amount of your next bill, enter 0 to end. $'))
#The print statements show the amount of money left and the total of all the bills
print('The total amount of your monthly bills is $',total_bills)
print('the amount you will have left after paying bills is $',amt_left)
        
# Use comments liberally throughout the program. 