
def count_holes(n):
    if type(n) != int and type(n) != str:
        print('ERROR_1')

    else:
        try:
            dictionary = {'9': 1, '8': 2, '6': 1, '4': 1, '0': 1}
            counter_holes = 0
            n = int(n)  # видаляє зайві "0" на початку
            n = str(n)

            for i in n:
                if i in dictionary:
                    counter_holes += dictionary.get(i)
            print(counter_holes)

        except ValueError:
            print('ERROR_2')
        except TypeError:
            print('ERROR_3')


count_holes(n='')


