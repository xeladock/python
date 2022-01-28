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
res=matrix = [ [ "." for i in range(a) ] for j in range(b) ]
matrix=[]; row=0
tmp=[]
while row!=a:
    matrix.append(list(input())); row+=1
# s=[]
# for m in matrix:
#    s.append()
# matrix[0][0]='AAAAA'
# print(matrix)
for m in matrix:
    # m.insert(-1,m[0])
    m.append(m[0])
    m.insert(0,m[len(m)-2])
    # print(m)
# s=matrix[0]
# matrix.insert(-1,s)
matrix.append(matrix[0])
matrix.insert(0,matrix[len(matrix)-2])
# tmp.extend(matrix)
# tmp[1][0]='0'
# print(tmp)
# test=[]
# for m in matrix:
#     m[0]=10
#     break
# matrix[0][0]='AAAA'

for cres in range(len(matrix)):
    for sres in range(len(matrix[0])):
        print([cres][sres])
        break
    break
print(matrix)
    # test.append(m)
# test[0][0]='0'
# print(test)
# for m in matrix:
#     m[0]='0'
#     m[-1]='0'
#     break

# for i in range(len(matrix)):
#     print(i)

# test[0][0]='0';
# test[5][0]='.'
# print(test)
# matrix[0][-1]='0';
# matrix[-1][0]='0';
# matrix[-1][-1]='0'
# for cres in range(a[0]):
#     for sres in range(a[1]):
# print(matrix)


# for cres in range(len(matrix)):
#     for sres in range(len(matrix[0])):
#
#         # if matrix[cres][sres]=='X':
#             tmp2 = []
#             tmp2.append(matrix[cres-1][sres-1]);
#             tmp2.append(matrix[cres - 1][sres]);
#             tmp2.append(matrix[cres - 1][sres + 1])
#             tmp2.append(matrix[cres][sres - 1]);tmp2.append(matrix[cres][sres + 1])
#             tmp2.append(matrix[cres + 1][sres - 1]); tmp2.append(matrix[cres + 1][sres]); tmp2.append(matrix[cres + 1][sres + 1])
#             tmp.append(tmp2)

            # print(tmp)
# for m in matrix:
#     print(*m)

# print(tmp)
# print(len(tmp))
# for cres in range(a[0]):
#     for sres in range(a[1]):
#         if matrix[cres][sres]=='*': matrix[cres][sres]=999
#         else:                       matrix[cres][sres]=0
# for m in matrix: m.insert(0,0); m.append(0)
# matrix.insert(0, [0 for i in range(len(matrix[0]))])
# matrix.append([ 0 for i in range(len(matrix[0]))])
# for cres in range(1,a[0]+1):
#     for sres in range(1,a[1]+1):
#         if matrix[cres][sres]>=999:
#             matrix[cres-1][sres-1]+=1; matrix[cres - 1][sres]+=1; matrix[cres - 1][sres + 1]+=1
#             matrix[cres][sres - 1]+= 1; matrix[cres][sres + 1]+=1
#             matrix[cres + 1][sres - 1]+=1; matrix[cres + 1][sres]+=1; matrix[cres + 1][sres + 1]+=1
# for cres in range(1,a[0]+1):
#     for sres in range(1,a[1]+1):
#         print('*' if matrix[cres][sres]>=999 else str(matrix[cres][sres]),end='')
#     print()