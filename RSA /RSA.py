__author__ = 'sr1k4n7h'

import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def euclid_mul_inv(e, phi):
    c, x1, y1, x2 = 0, 0, 1, 1
    _phi = phi

    while e > 0:
        a = _phi / e
        b = _phi - a * e
        _phi, e = e, b
        x = x2 - a * x1
        y = c - a * y1
        x2, x1 = x1, x
        c, y1 = y1, y

    if _phi == 1:
        return c + phi


def main():
    p = int(raw_input("Enter a prime number (P): "))
    q = int(raw_input("Enter another prime number (Q) != (P): "))

    flag = False if p != q else True
    while flag:
        print("P & Q must be different ! Enter Again ! ")
        p = int(raw_input("Enter a prime number (P): "))
        q = int(raw_input("Enter another prime number (Q) != (P): "))
        flag = False if p != q else True

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = euclid_mul_inv(e, phi)

    message = int(raw_input("Enter a message (number) to Encrypt: "))
    encrypted_msg = (message ** e) % n
    print "Encrypted message with Private Key: " + str(encrypted_msg)
    decrypted_msg = (encrypted_msg ** d) % n
    print "Decrypted message with Public Key :" + str(decrypted_msg)


if __name__ == '__main__':
    main()
