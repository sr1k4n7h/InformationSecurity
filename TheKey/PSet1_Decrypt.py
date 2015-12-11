__author__ = 'sr1k4n7h'

from string import ascii_lowercase as l, ascii_uppercase as u


def ceaser_cipher(text, key):
    decrypted = ''
    for i in text:
        if i in l:
            decrypted += l[(l.index(i) - key) % 26]
        elif i in u:
            decrypted += u[(u.index(i) - key) % 26]
        else:
            decrypted += i
    return decrypted

print("Caesar - Decrypted Text : " + str(ceaser_cipher(input("Enter the Plain Text : "), int(input("Enter the Key : ")))))
