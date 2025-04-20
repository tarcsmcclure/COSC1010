#
# Anna McClure
# 4-20-25
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#main function

def main():
    #get user input
    user_sentence = input('Type a sentence in English to be converted to Pig Latin: ')
    if len(user_sentence) == 0:
        print('Error, please type a sentence')
        return
    
    words = user_sentence.split()
    pig_latin = []
    for word in words:
        new_word = word[1:] + word[0] + "AY"
        pig_latin.append(new_word)
   
    #show results
    print('English: ', user_sentence)
    print('Pig Latin: ', ' '.join(pig_latin))

if __name__ == '__main__': main()