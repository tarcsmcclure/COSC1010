#Assume a file containing a series of integers is named `numbers.txt` and exists on the computer’s disk. 
#Write a program that calculates the average of all the numbers stored in the file.
# Anna McClure
# 3/29/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
def main():
    sum = 0.0
    #open the numbers file
    with open ('numbers.txt', 'r') as numbers_file:
        #read the first number in file
        for line in numbers_file:
            total = float(line)
            sum += total

    print(f'{sum:,.2f}')

if __name__ == '_main_':
    main()
      