decode = {
    '!': 'A', '1': 'a', '@': 'B', '2': 'b', '#': 'C', '3': 'c', '$': 'D', '4': 'd', '%': 'E', '5': 'e',
    '^': 'F', '6': 'f', '&': 'G', '7': 'g', '*': 'H', '8': 'h', '(': 'I', '9': 'i', ')': 'J', '0': 'j',
    '~': 'K', '`': 'k', '{': 'L', '[': 'l', '<': 'M', '>': 'm', '?': 'N', '/': 'n', '+': 'O', '=': 'o',
    '_': 'P', '-': 'p', ':': 'Q', ';': 'q', '|': 'R', ',': 'r', '.': 'S', ']': 's', '"': 'T', '}': 't',
    'V': 'U', 'A': 'u', 'W': 'V', 'B': 'v', 'X': 'W', 'C': 'w', 'Y': 'X', 'D': 'x', 'Z': 'Y', 'E': 'y',
    'F': 'Z', 'G': 'z'
}
def main():
    try:
        with open('encrypted.txt', 'r') as decoded_file:
            for char in decoded_file.read():
                    if char in decode:
                        print(decode[char])
                    else:
                        print(char, end='')
    except FileNotFoundError:
        print('Error encrypted.txt not found')

if __name__ == '__main__': main()
