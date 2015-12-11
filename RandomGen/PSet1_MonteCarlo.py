__author__ = 'sr1k4n7h'

import random
from datetime import datetime

f = open("PSet1_MonteCarlo.txt", "w+")
random_nums = [random.randint(1, 100) for _ in range(1000)]  # List of 100 random numbers in range 1 - 100
for i in random_nums:
    # 1. Performing addition operation between array element and the seed (time) to generate another random number
    # 2. Creating binary number sequence, and storing it in the "PSet1_MonteCarlo.txt" file.
    f.write(str(bin(i + datetime.now().microsecond))[2:])
    f.write("\n")
f.close()
