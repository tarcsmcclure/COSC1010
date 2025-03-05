#
# Anna McClure
# 3-5-25
# Feet to Inches Programming Project
# COSC 1010
#
#constant for the number of inches per feet
INCHES_PER_FOOT = 12

#main function
def main():
    #get a number of feet from user
    feet = int(input('Enter the number of feet: '))
    
    #convert to inches
    print(feet,'feet', 'equals', feet_to_inches(feet), 'inches')

#the feet_to_inches function converts
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
    
#call main
main()
