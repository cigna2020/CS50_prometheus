from typing import List


def cash():
    change = input('Numbers ')
    money: List[float] = [0.25, 0.10, 0.5, 0.1]
    counter = 0
    while True:
        if change.isnumeric():
            break
    while float(change) > 0:
        if float(change) >= float(money[0]):
            change = float(change) - money[0]
            counter += 1
            print(change, counter)


cash()




