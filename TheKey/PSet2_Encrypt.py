__author__ = 'sr1k4n7h'


def columnar_transposition(text, key):
    encrypted = ''
    for i in range(key):
        encrypted += text[i::key]  # OBTAINING THE LETTERS IN COLUMNS THROUGH LIST SLICING
    return encrypted

print("COLUMNAR TRASNSPOSITION - ENCRYPTED TEXT : " + columnar_transposition(input("ENTER THE PLAIN TEXT : "),
                                                                             int(input("ENTER THE KEY (>1) : "))))
