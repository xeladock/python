# Напишите программу, вычисляющую следующее состояние поля для Game of life.
#
# Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного конца (поле представляет собой тор).
#
# Формат ввода:
#
# На первой строке указаны два целых числа через пробел -- высота и ширина поля.
# В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую.
#
# Формат вывода:
# Следующее состояние поля, используя те же обозначения, что использовались на вводе.
#
# Sample Input 1:
#
# 5 5
# .....
# ..X..
# ...X.
# .XXX.
# .....
# Sample Output 1:
#
# .....
# .....
# .X.X.
# ..XX.
# ..X..
# Sample Input 2:
#
# 5 5
# .....
# .....
# .XXX.
# .....
# .....
# Sample Output 2:
#
# .....
# ..X..
# ..X..
# ..X..
# .....
# Sample Input 3:
#
# 5 6
# ...XX.
# .XX...
# ..X...
# XX....
# X..XX.
# Sample Output 3:
#
# .X..XX
# .XX...
# X.X...
# XXXX.X
# XXXXX.

# https://stepik.org/lesson/22778/step/1?adaptive=true&unit=5351

a, b = map(int, input().split())
matrix=[]; tmp=[]
for i in range(a):
    matrix.append(list(input()))
for m in matrix:
    m.append(m[0])
    m.insert(0,m[len(m)-2])
matrix.append(matrix[0])
matrix.insert(0,matrix[len(matrix)-2])

for cres in range(1,len(matrix)-1):
    for sres in range(1,len(matrix[0])-1):
            tmp2 = []
            tmp2.append(matrix[cres][sres])
            tmp2.append(matrix[cres-1][sres-1]);
            tmp2.append(matrix[cres - 1][sres]);
            tmp2.append(matrix[cres - 1][sres + 1])
            tmp2.append(matrix[cres][sres - 1]);tmp2.append(matrix[cres][sres + 1])
            tmp2.append(matrix[cres + 1][sres - 1]); tmp2.append(matrix[cres + 1][sres]); tmp2.append(matrix[cres + 1][sres + 1])
            tmp.append(tmp2)
i=0
for x in tmp:
        i+=1
        if (x[0]=='.') and (x.count('X')==3):
            print('X',end='')
        elif (x[0]=='X') and (x.count('X')==3 or x.count('X')==4):
            print('X',end='')
        elif (x[0]=='X') and (x.count('X')<3 or x.count('X')>4):
            print('.',end='')
        else: print(x[0],end='')
        if i == b: print(); i = 0
