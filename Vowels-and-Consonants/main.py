#
# Anna McClure
# 4-20-25
# Vowels and Consonants Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#main fucntion
def main():
    #get a string from the user
    user_str = input('Enter a string of characters: ')

    #report the vowels and consonants
    print('That string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')

#the num_vowels function returns the number of vowels  in the string passed to an argument
def num_vowels(s):
    #list containing the vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    #initilize an accumulator
    v_count = 0

    #Count the vowels
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1
    #return the vowel count
    return v_count

# num_consonants function returns the number of consonants in teh string passed as an arugument
def num_consonants(s):
    #make a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    #initialize accumulator
    c_count = 0

    # count the consonants in s
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1
    #return the consonant counter
    return c_count

main()