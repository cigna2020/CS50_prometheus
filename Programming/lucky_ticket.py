import sys


def lucky_ticket():
    a = sys.argv[1]
    b = sys.argv[2]
    d = 0
    c = 0
    counter = 0

    while int(a) <= int(b):
        if len(str(a)) <= 6:
            a = (6 - len(str(a))) * '0' + str(a)
        for i in a[-3:]:
            d += int(i)
        for j in a[:3]:
            c += int(j)
        if int(d) == int(c):
            counter += 1
        d = int(d) * 0
        c = int(c) * 0
        a = int(a) + 1
        continue
    print(counter)


lucky_ticket()