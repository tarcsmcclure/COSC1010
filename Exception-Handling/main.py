# Anna McClure
# 3/30/25
# Exception Handling Programming Project
# COSC 1010
# Use comments liberally throughout the program. 
# begin program
def main():
    # initialize sum variable
    sum = 0.0
    # initialize counter for number of values
    count = 0
    
    try:
        # open the numbers file
        with open('numbers.txt', 'r') as numbers_file:
            # begin reading data in file
            for line in numbers_file:
                # variable named total set to float for each line
                total = float(line)
                # variable sum adds numbers together
                sum += total
                # increment counter for each number
                count += 1
            
        # calculate average
        average = sum / count if count > 0 else 0
    
        # print results with formatting
        print(f'The average is: {average:,.2f}')
    except FileNotFoundError:
        print('An error occured trying to read the file.')
    
    except ValueError:
        print('Non-numeric data found in the file.')

    except:
        print('An error occured.')
    # calls function
if __name__ == '__main__':    # corrected from '_main_' to '__main__'
        main()
