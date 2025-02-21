#
# Anna McClure
# 2/20/25
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Global Variables
people = 0
HD_per_person = 0
hotdogs = 10
buns = 8
totalHD = 0
totalBuns = 0
leftover_HD = 0
leftover_buns = 0
remainder = 0  
remainder_buns = 0 

# Prompt user for total people attending cookout
people = int(input('Enter the number of people attending the cookout: '))

# Prompt user for total hot dogs per person
HD_per_person = int(input('Enter the amount of hot dogs each person will consume: '))

# Calculate total number of hot dogs needed
totalHD = (people * HD_per_person) // hotdogs

# Calculate the number of packages of buns needed
totalBuns = (people * HD_per_person) // buns

# Calculate remainder of hotdogs and round up
if (people * HD_per_person) % hotdogs > 0:
    remainder = 1  

# Setting new total to the total hotdogs plus 1 to round up to the even amount of packages
newTotal = totalHD + remainder

if (people * HD_per_person) % buns > 0:
    remainder_buns = 1  

newTotal_Buns = totalBuns + remainder_buns

print("The minimum number of hot dog packages required is", newTotal)
print("The minimum number of packages of hot dog buns required is", newTotal_Buns)

# Calculate leftovers
HD = people * HD_per_person
leftover_HD = (newTotal * hotdogs) - HD
print("The number of hot dogs that will be left over is", leftover_HD)

BN = people * HD_per_person
leftover_buns = (newTotal_Buns * buns) - BN
print("The number of hot dog buns that will be left over is", leftover_buns)