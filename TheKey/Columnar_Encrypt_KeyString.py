__author__ = 'sr1k4n7h'

import re

# def sort_indices(word):               #  FAILING FOR DUPLICATE LETTERS IN THE KEY
#    """ sorting the indices in the key """
#     h, k = {}, 0
#     for i in sorted(word):
#         h.__setitem__(i, k)
#         k += 1
#     return [h[i] for i in word]

# SORTING THE INDICES OF THE KEY
sorted_indices = lambda key: [f[1] for f in sorted([(k[1], i) for i, k in enumerate(sorted([(key[i], i) for i in range(len(key))]))])]


def columnar_transposition(text, keyword):
    text = re.sub('[^A-Z]', '', text.upper())  # REMOVING ALL THE PUNCTUATIONS, WHITESPACES AND CONVERTING TO UPPER CASE
    indices = sorted_indices(keyword)
    key_length = len(keyword)
    encrypted = ''
    for i in range(key_length):
        encrypted += text[indices.index(i)::key_length]  # OBTAINING THE LETTERS IN COLUMNS THROUGH LIST SLICING
    return encrypted


print("COLUMNAR TRASNSPOSITION - ENCRYPTED TEXT : " + columnar_transposition(input("ENTER THE PLAIN TEXT : "),
                                                                             input("ENTER THE KEY STRING: ")))
