# Имеется реализованная функция f(x)f(x), принимающая на вход целое число xx, которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
#
# Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного аргумента xx.
#
# Напишите программу, которая вычисляет значение этой функции для nn чисел.
#
# Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
#
# Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода на тесте.
#
# Формат ввода:
# На первой строке находится число nn -− количество значений, на которых нужно посчитать функцию. После этого следует nn строк, на каждой строке по одному целому числу.
#
# Формат вывода:
# nn строк, в каждой из которой результат вычисления функции на соответствующем аргументе.
#
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41

# https://stepik.org/lesson/21211/step/2?adaptive=true&unit=5097

# n=int(input())
# a=[list(map(int, input().split())) for _ in range(n)]
# a=[item for sublist in [list(map(int, input().split())) for _ in range(int(input()))] for item in sublist]
# for n in a:
#     print(n*2)
# print(a)
# def cal(x):
#     s=[]
#     for aa in a:
#         # x = aa * 2
#         return s.append(aa*2)
# print(cal(5))
import random
def calc(a):
    s=a*2
    return s

# n=int(input())
d={}

c=[]
for i in range(int(input())):
    s = int(input())
    if s in d.keys():
        d.update({random.random(): d.get(s)})
    else:

        d.setdefault(s, calc(s))


print(d)
print(*d.values(),end='\n')
# print(s)

# for key, value in d.items():
#     if key in s:
#         print(value)

# for ss in s:
#     if ss in d.keys():
#         print(d.get(ss))

# print(d)
# print(s)
