#Assume a file containing a series of integers is named `numbers.txt` and exists on the computer’s disk. 
#Write a program that calculates the average of all the numbers stored in the file.
# Anna McClure
# 3/29/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#begin program
def main():
    #initilize sum variable
    sum = 0.0
    #open the numbers file
    with open ('numbers.txt', 'r') as numbers_file:
        #begin reading data in file
        for line in numbers_file:
            #variable named total set to float for each line
            total = float(line)
            #variable sum adds numbers together
            sum += total
            
    #prints results
    print(f'{sum:,.2f}')
#calls function
if __name__ == '_main_':
    main()
      
