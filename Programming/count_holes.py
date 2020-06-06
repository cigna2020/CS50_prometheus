
def count_holes(n):
    dictionary = {'9': 1, '8': 2, '6': 1, '4': 1, '0': 1}
    counter_holes = 0
    if type(n) != int and type(n) != str:
        print('ERROR')

    else:
        for i in str(n):
            if str(i) in dictionary:
                counter_holes += dictionary.get(i)
        print(counter_holes)

count_holes(906)


