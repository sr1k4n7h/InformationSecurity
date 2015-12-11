__author__ = 'sr1k4n7h'

import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primes_factors(n):
    pf_list = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            pf_list.append(d)
            n //= d
        d += 1
    if n > 1:
        pf_list.append(n)
    return pf_list


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
    e = 17
    n = [238981, 18067901, 2705314597, 225929304371, 13642478275813]
    t = []
    for k in n:
        pf = primes_factors(k)
        flag = False
        for i in pf:
            p = i
            q = k / p
            if q in pf:
                t.append((p, q))
                break
    for i in t:
        p, q = i
        n = p * q
        phi = (p - 1) * (q - 1)
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)
        d = euclid_mul_inv(e, phi)
        print("Cracked D Value : " + str(d))


if __name__ == '__main__':
    main()
