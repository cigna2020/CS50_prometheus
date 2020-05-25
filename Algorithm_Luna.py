def sum_multiplied_2(card):
    count = 0
    str_card = str(card)
    numbers_with_step = int(str_card[::2])
    for i in str(numbers_with_step):
        count += int(i) * 2
    print(count)

probe_1 = sum_multiplied_2(card = 4003600000000014)








