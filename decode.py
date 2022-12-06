from termcolor import cprint
import UI


def validate(key, ct):
    if len(ct) % len(key):
        return False
    return True


def make_matrix(key, ct):
    matrix = {}
    message = ''
    kh = len(ct) // len(key)
    print(kh, 'key')
    l = []
    skey = sorted(key)
    ki = 0
    print(key)
    for i, v in enumerate(ct):
        message += v
        l.append(v)
        print(i % kh)
        if i % kh == kh-1 and not i == 0:
            print(l)
            matrix[skey[ki]] = l
            ki += 1
            l = []
    return matrix


def decode():
    while True:
        key = input("Enter key: ")
        ciphertext = input("Enter Ciphertext: ")
        # key = 'MEGA'                # 3120
        # ciphertext = 'dhbfcgae'     # abcdefgh
        if validate(key, ciphertext):
            matrix = make_matrix(key, ciphertext)
            message = UI.show_matrix(matrix, key)
            print(f'The encrypted message is: \n{message}')
        else:
            print("Invalid key ciphertext pair")
        break


if __name__ == '__main__':
    decode()
