#
# Anna McClure
# 4/14/25
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
#import random
import random
#begin program
def main():
    #open the file
    with open('8_ball_responses.txt', 'r') as responses_file:
        #build empty list
        responses = []
        for line in responses_file:
            responses.append(line.strip())
    while True:
        question = input('What is your question? Press \'q\' to quit ')
        if question == "q":
            break
        else:
            print(f'The answer to your question is: {random.choice(responses)}')
    print('Thanks for playing the Magic 8 Ball')

if __name__ == '__main__':
 main()