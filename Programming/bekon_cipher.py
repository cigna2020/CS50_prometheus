import sys


def bekon_cipher():
    key = 'aaaaabbbbbabbbaabbababbaaababaab'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a = str(sys.argv[1:])

    for sign in a:
        if sign == ' ':
            sign = ''

    step = ''
    for i in a:
        if i.islower():
            step = step + 'a'
        elif i.isupper():
            step = step + 'b'

    part = str
    list = []
    start = 0
    end = 5
    for i in alphabet:
        part = key[start:end]
        list.append(part)
        start = start + 1
        end = end + 1

    start_1 = 0
    start_2 = 5
    list_2 = ()
    list_3 = ''
    result = ''
    length = ''
    j = 1
    while j < len(a):
        length = step[start_1:start_2]
        if len(length) == 5:
            list_2 = list.index(length)
            list_3 = alphabet[list_2]
            result = result + list_3
        j = j + 1
        start_1 = start_1 + 5
        start_2 = start_2 + 5

    print(result)

bekon_cipher()