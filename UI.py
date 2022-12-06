from termcolor import cprint


def show_matrix(matrix, key):
    message = ''
    letter = ''
    for i in key:
        cprint(i, 'red', end='\t', flush=True)
    print()
    kl = len(key)
    ml = len(key) * len(matrix[key[0]])
    l = 0
    for i in range(ml):
        if i % kl == 0 and not i == 0:
            l += 1
            print()
        letter = matrix[key[i % kl]][l]
        message += letter
        cprint(letter, 'green', end='\t', flush=True)
    print()
    return message
