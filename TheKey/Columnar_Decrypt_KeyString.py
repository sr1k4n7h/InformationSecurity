__author__ = 'sr1k4n7h'

import re

# UNSORTED THE INDICES OF THE KEY
unsorted_indices = lambda key: [f[1] for f in sorted([(key[i], i) for i in range(len(key))])]


def columnar_transposition(text, keyword):
    text = re.sub('[^A-Z]', '', text.upper())  # REMOVING ALL THE PUNCTUATIONS, WHITESPACES AND CONVERTING TO UPPER CASE
    decrypted = [''] * len(text)
    t, k, j = len(text), len(keyword), 0
    indices = unsorted_indices(keyword)
    print(indices)
    for i in range(len(keyword)):
        decrypt_columns = int(t / k)
        if indices[i] < t % k:
            decrypt_columns += 1
        decrypted[indices[i]::k] = text[j:j + decrypt_columns]
        j += decrypt_columns
        print(decrypted)
    return ''.join(decrypted)


print("COLUMNAR TRASNSPOSITION - DECRYPTED TEXT : " + columnar_transposition(input("ENTER THE ENCRYPTED TEXT : "),
                                                                             input("ENTER THE KEY STRING: ")))
