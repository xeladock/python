# Поле для игры сапёр представляет собой сетку размером n \times mn×m. В ячейке сетки может находиться или отсутствовать мина.
#
# Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)
#
# Формат ввода:
# На первой строке указываются два натуральных числа 1 \le n,m \le 1001≤n,m≤100, после чего в nn строках содержится описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.
#
# Формат вывода:
# nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), при этом число означает количество мин в соседних ячейках поля.
#
# Sample Input:
#
# 4 4
# ..*.
# **..
# ..*.
# ....
# Sample Output:
#
# 23*1
# **32
# 23*1
# 0111

# https://stepik.org/lesson/21980/step/1?adaptive=true&thread=solutions&unit=5239

a=[int(x) for x in input().split()]
if len(a)!=2: print('Invalid data'); exit()
matrix=[]
row=0
while row!=a[0]:
    column=list(input())
    matrix.append(column)
    if len(column)!=a[1]: print('\ninvalid data'); exit()
    row+=1
for cres in range(a[0]):
    for sres in range(a[1]):
        if matrix[cres][sres]=='*':
            matrix[cres][sres]=999
        else:
            matrix[cres][sres]=0
for m in matrix:
    m.insert(0,0)
    m.append(0)
matrix.insert(0, [0 for i in range(len(matrix[0]))])
matrix.append([ 0 for i in range(len(matrix[0]))])
for cres in range(1,a[0]+1):
    for sres in range(1,a[1]+1):
        if matrix[cres][sres]>=999:
            matrix[cres-1][sres-1]+=1; matrix[cres - 1][sres]+=1; matrix[cres - 1][sres + 1]+=1
            matrix[cres][sres - 1]+= 1; matrix[cres][sres + 1]+=1
            matrix[cres + 1][sres - 1]+=1; matrix[cres + 1][sres]+=1; matrix[cres + 1][sres + 1]+=1
for cres in range(1,a[0]+1):
    for sres in range(1,a[1]+1):
        print('*' if matrix[cres][sres]>=999 else str(matrix[cres][sres]),end='')
    print()
# print(res)


a=[int(x) for x in input().split()]
matrix=[]; row=0
while row!=a[0]:
    matrix.append(list(input())); row+=1
for cres in range(a[0]):
    for sres in range(a[1]):
        if matrix[cres][sres]=='*': matrix[cres][sres]=999
        else:                       matrix[cres][sres]=0
for m in matrix: m.insert(0,0); m.append(0)
matrix.insert(0, [0 for i in range(len(matrix[0]))])
matrix.append([ 0 for i in range(len(matrix[0]))])
for cres in range(1,a[0]+1):
    for sres in range(1,a[1]+1):
        if matrix[cres][sres]>=999:
            matrix[cres-1][sres-1]+=1; matrix[cres - 1][sres]+=1; matrix[cres - 1][sres + 1]+=1
            matrix[cres][sres - 1]+= 1; matrix[cres][sres + 1]+=1
            matrix[cres + 1][sres - 1]+=1; matrix[cres + 1][sres]+=1; matrix[cres + 1][sres + 1]+=1
for cres in range(1,a[0]+1):
    for sres in range(1,a[1]+1):
        print('*' if matrix[cres][sres]>=999 else str(matrix[cres][sres]),end='')
    print()