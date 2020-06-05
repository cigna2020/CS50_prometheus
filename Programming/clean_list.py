import sys


def clean_list(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
        if i in new_list:
            if type(i) != type(new_list[new_list.index(i)]):
                new_list.append(i)
    return new_list


check = list(sys.argv[1:])
print(clean_list(check))


