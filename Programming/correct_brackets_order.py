import sys


def brackets():
    brackets = sys.argv[1]
    signs_number_1 = 0
    signs_number_2 = 0
    error = 0
    for sign in brackets:
        if sign == '(':
            signs_number_1 += 1
        if sign == ')':
            signs_number_2 += 1
        if signs_number_2 > signs_number_1:
            print('NO')
            error += 1
            break

    if signs_number_2 == signs_number_1 and error == 0:
        print('YES')
    if signs_number_2 != signs_number_1 and error == 0:
        print('NO')

brackets()



