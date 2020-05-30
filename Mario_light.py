def Mario():
    while True:
        number = input('What is your number? ')
        if number.isnumeric():
            if 1 <= int(number) <= 8:
                break
    for i in range(int(number)):
        for j in range(int(number) - i - 1):
            print(' ', end='')
        for k in range(i + 1):
            print('#', end='')
        print('')

fun = Mario()