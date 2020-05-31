from math import floor
from typing import List


def cash():
    money = [25, 10, 50, 1]
    counter = 0
    numb = input('Numbers ')
    change = floor(float(numb) * 100)

    while float(change) > 0:

        i = 0
        if float(change) >= float(money[i]):
            change = float(change) - float(money[i])
            counter += 1
        else: i += 1
    print(counter)


cash()




