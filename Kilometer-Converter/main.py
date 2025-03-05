#
# Anna McClure
# 3-5-25
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#This program converts kilometers to miles. 
CONVERSION_FACTOR = 0.6214

#The main function gets a distance in kilometers and calls the show_miles function to convert it.
def main():
	#get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))
    
    #display the distance converted to miles. 
    show_miles(kilometers)

#the show_miles function converts the parameter km from kilometers to miles and siplays the result.
def show_miles(km):
    #calculate miles
    miles = km * CONVERSION_FACTOR
    
    #display the miles
    print(km, 'kilometers equals', miles, 'miles.')

#call the main function
main()