
def clean_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

clean_list([32, 32.1, 32.0, -123])


