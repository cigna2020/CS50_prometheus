

def counter_a_b(a, b):
    unique_list_a = []
    unique_list_b = []
    for i in str(a):
        if i not in unique_list_a:
            unique_list_a.append(i)
    for j in str(b):
        if j not in unique_list_b:
            unique_list_b.append(j)
    print(unique_list_b, unique_list_a)

counter_a_b(1233211, 12128)