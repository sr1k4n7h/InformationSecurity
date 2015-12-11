__author__ = 'sr1k4n7h'

import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541]  # List of first 100 primes

f = open("PSet1_MersennePrime.txt", "w+")

# mersenne = lambda x: pow(2, x) - 1
# ran = [mersenne(i) for i in primes]  # List of first 100 Mersenne Primes

mersenne_primes = [(1 << i) - 1 for i in primes]  # List of first 100 Mersenne Primes through BitManipulation

for i in mersenne_primes:
    # 1. Selecting seed as the mersenne prime number to generate random number
    # 2. Creating binary number sequence, and storing it in the "PSet1_MersennePrime.txt" file.
    random.seed(i)
    f.write(str(bin(int(str(random.random())[2:])))[2:])
    f.write("\n")

f.close()
