__author__ = 'sr1k4n7h'


def columnar_transposition(text, key):
    decrypted = [''] * len(text)
    text_len, j = len(text), 0
    for i in range(key):
        decrypt_columns = int(text_len / key)
        if i < text_len % key:
            decrypt_columns += 1
        decrypted[i::key] = text[j:j + decrypt_columns]  # OBTAINING DECRYPTED LETTERS IN COLUMNS THROUGH LIST SLICING
        j += decrypt_columns
    return ''.join(decrypted)


print("COLUMNAR TRANSPOSITION - DECRYPTED TEXT : " + columnar_transposition(input("ENTER THE ENCRYPTED TEXT : "),
                                                                            int(input("ENTER THE KEY (>1) : "))))
