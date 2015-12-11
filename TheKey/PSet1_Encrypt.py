__author__ = 'sr1k4n7h'

from string import ascii_lowercase as l, ascii_uppercase as u


def ceaser_cipher(text, key):
    encrypted = ''
    for i in text:
        if i in l:
            encrypted += l[(l.index(i) + key) % 26]
        elif i in u:
            encrypted += u[(u.index(i) + key) % 26]
        else:
            encrypted += i
    return encrypted

print("Caesar - Encrypted Text : " + str(ceaser_cipher(input("Enter the Plain Text : "), int(input("Enter the Key : ")))))
