# v.1 обійти вкладені списки і порівняти їх довжину, пересвідчуючись при цьому, що всі структури є списками

mat = [[1, 2, 3, 0, 0], [1, 7], [4, 9, 2], [6, 2, 5]]

def is_matrix(mat):
    if not isinstance(mat, list) or not isinstance(mat[0], list):
        return False
    size = len(mat[0])
    for row in mat:
        if not isinstance(row, list) or len(row) != size:
            return False
    return True

# v.2 обійти всі елементи матриці, використовуючи подвійний цикл, вивести всі елементи матриці:

def print_elements(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j])

print_elements(mat=mat)

# v.3 вивести матрицю у вигляді прямокутника:

def output_matrix(mat):
    for row in mat:
        string = ''
        for el in row:
            string = string + "%4d" % (el)
        print(string)

# v.4 виводить новий список який складається з відповідних елементів попереднього списку, тобто new_list = [[old_list[0][1], old_list[1][1]...]]

def transpone(mat):
    mat2 = []
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if j==0:
                mat2.append([])
            mat2[i].append(mat[j][i])
    print(mat2)
