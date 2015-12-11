__author__ = 'sr1k4n7h'

import random
from datetime import datetime

f = open("PSet1_Library.txt", "w+")
for _ in range(1001):
    # 1. Considering the microseconds as the Seed. milliseconds seems repetitive & producing same pseudo-random numbers
    random.seed(datetime.now().microsecond)
    # 1. Considering only the decimal part of random number  ## i.e ignoring "0." of every number.
    # 2. Ignoring the python-default "0b" of the binary conversion.
    # 3. Creating binary number sequence, and storing it in the "PSet1_Library.txt" file.
    f.write(str(bin(int(str(random.random())[2:])))[2:])
    f.write("\n")
f.close()
