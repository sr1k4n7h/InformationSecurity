__author__ = 'sr1k4n7h'


def substitution_cipher(text, key):
    H = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
         'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
         'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    alphabets = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z')

    key = key.upper()
    if len(key) < 26:
        key += ''.join(sorted(set("ABCDEFGHIJLMNOPQRSTUVWXYZ").difference(key)))
    inverted_key = ''
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        inverted_key += alphabets[(key.index(i)) % 26]
    decrypt = ''
    for c in text.upper():
        if c.isalpha():
            decrypt += inverted_key[H[c]]
        else:
            decrypt += c
    return decrypt


print("SIMPLE SUBSTITUTION - DECRYPTED TEXT : " + substitution_cipher(input("ENTER THE PLAIN TEXT : "),
                                                                      input("ENTER THE KEY STRING : ")))
