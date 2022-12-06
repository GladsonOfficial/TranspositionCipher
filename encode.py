from termcolor import cprint
import UI


def get_key():
    while True:
        key = input("Enter key: ")
        if not len(set(key)) == len(key):
            cprint('\tinvaild key\n', 'red')
        else:
            return key


def get_matrix(key, message):
    matrix = {}
    ki = 0
    for i in key:
        matrix[i] = []

    for i in message:
        l = matrix[key[ki]]
        l.append(i)
        matrix[key[ki]] = l

        ki += 1
        if ki >= len(key):
            ki = 0
    return matrix


def generate_seq(n):
    s = ''
    li = 0
    for i in range(n):
        s += chr((i % 26) + 97)
    return s


def adjust_message_length(keylen, message):
    off = keylen - (len(message) % keylen)
    # print('offset: ', off)
    if not off == keylen:
        message = message + generate_seq(off)
    return message


def get_ciphertext(key, matrix):
    skey = sorted(key)
    s = ''
    for i in skey:
        for j in matrix[i]:
            s += j
    return s


def encode():
    key = get_key()
    message = input("Enter Message: ")
    message = adjust_message_length(len(key), message)
    while True:
        matrix = get_matrix(key, message)
        UI.show_matrix(matrix, key)
        print(f'Ciphertext: \n{get_ciphertext(key, matrix)}')

        print('\n1. Change Key')
        print('2. Change Message')
        print('0. exit')
        choice = input("Enter Choice: ")
        if choice == '1':
            key = get_key()
        if choice == '2':
            message = input("Enter Message: ")
            message = adjust_message_length(len(key), message)
        if choice == '0':
            break
        else:
            print('invalid option')


if __name__ == '__main__':
    encode()
