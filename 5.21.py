# Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.
#
# Формат ввода:
# В первой строке указываются два целых числа nn и mm, количество строк и столбцов, соответственно.
# Далее следуют nn строк, содержащих по mm целых чисел, разделённых пробелом.
#
# Формат вывода:
# Программа должна вывести mm строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.
#
# Sample Input 1:
#
# 2 3
# 1 2 3
# 4 5 6
# Sample Output 1:
#
# 1 4
# 2 5
# 3 6
# Sample Input 2:
#
# 2 2
# 1 2
# 3 4
# Sample Output 2:
#
# 1 3
# 2 4

# https://stepik.org/lesson/22792/step/1?adaptive=true&thread=solutions&unit=5352
import numpy as np
a, b = map(int, input().split())
# m=0
matrix=[]
for i in range(a):
    d=list(map(int, input().split()))
    if len(d) != b: print('error'); exit()
    matrix.append(d)
# for i in zip(matrix):

    # m+=1
# x.transpose((1,0))
# y=np.transpose(np.array(matrix))
[print(*yy) for yy in np.transpose(np.array(matrix))]
# print(y)
# for yy in y:
#     print(*yy)
# xx=list(map(list, zip(*map(lambda x: x[::-1], matrix))))
# matrix=[list(a) for a in zip(*matrix)]



