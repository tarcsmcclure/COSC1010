#
# Anna McClure
# 4-20-25
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#build dictionary for letters, encrypting them to a special character
codes = {
    'A': '!', 'a': '1', 'B': '@', 'b': '2', 'C': '#', 'c': '3', 'D': '$', 'd': '4', 'E': '%', 'e': '5',
    'F': '^', 'f': '6', 'G': '&', 'g': '7', 'H': '*', 'h': '8', 'I': '(', 'i': '9', 'J': ')', 'j': '0',
    'K': '~', 'k': '`', 'L': '{', 'l': '[', 'M': '<', 'm': '>', 'N': '?', 'n': '/', 'O': '+', 'o': '=',
    'P': '_', 'p': '-', 'Q': ':', 'q': ';', 'R': '|', 'r': ',', 'S': '.', 's': ']', 'T': '"', 't': '}',
    'U': "'", 'u': 'A', 'V': 'B', 'v': 'C', 'W': 'D', 'w': 'E', 'X': 'F', 'x': 'G', 'Y': 'H', 'y': 'I',
    'Z': 'J', 'z': 'K'
}
def main():
    #try statement
    try:
        with open('text.txt', 'r') as input_file:
            with open('encrypted.txt', 'w') as output_file:
                for char in input_file.read():
                    if char in codes:
                        output_file.write(codes[char])
                    else:
                        output_file.write(char)
    except FileNotFoundError:
        print('Error text.txt not found')


if __name__ == '__main__': main()

