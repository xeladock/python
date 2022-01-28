# Напишите программу, которая выводит nn первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
#
# Формат ввода:
# Строка, содержащая одно целое число nn, n \gt 0n>0.
#
# Формат вывода:
# Строка, содержащая требуемую последовательность чисел, разделённых пробелом.
#
# Sample Input:
#
# 7
# Sample Output:
#
# 1 2 2 3 3 3 4

# https://stepik.org/lesson/21974/step/2?adaptive=true&unit=5234

b=int(input())

# a=[int(i)*[i] for i in range (1,b+1)]
print(*[item for sublist in [int(i)*[i] for i in range (1,int(input())+1)] for item in sublist][:b])
# print(a[:5])
# print(a)