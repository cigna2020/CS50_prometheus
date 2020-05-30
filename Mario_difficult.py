def Mario():
    while True:
        number = input('What is your number? ')
        if number.isnumeric():
            if 1 <= int(number) <= 8:
                break
    for i in range(1, int(number) + 1):
        print(' ' * (int(number) - i))
        print('#' * i, end='')
        print(' ', end='')
        print('#' * i)

fun = Mario()