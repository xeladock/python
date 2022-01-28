# Напишите программу, которая находит все позиции вхождения подстроки в строку.
#
# Формат ввода:
# На первой строке содержится исходная строка, на второй строке ввода указана подстрока, позиции которой требуется найти. Строки состоят из символов латинского алфавита.
#
# Формат вывода:
# Строка, содержащая индексы (индексация начинается с нуля) вхождения подстроки в строку, разделённые пробелом или число -1 в случае, когда подстрока не найдена.
#
# Sample Input 1:
#
# abacabadaba
# aba
# Sample Output 1:
#
# 0 4 8
# Sample Input 2:
#
# aaaa
# aa
# Sample Output 2:
#
# 0 1 2
# Sample Input 3:
#
# abc
# d
# Sample Output 3:
#
# -1

# https://stepik.org/lesson/22777/step/1?adaptive=true&unit=5350

# import re
# a='abacabadaba'
# b='aba'
# pat=re.compile(b)
# for s in a:
#     for match in re.finditer(b,a):
#         print(a.find(b))
# a=re.split('(\d+)',b)
# res=re.findall(r'[[]',b)
# print(res)


#

# x=a.find(b)
# print(x)
# print(a)

# for b in a:
#     x=a.find(b)
#     print(x)
# .split(str(input()))

# a=str(input()).split(str(input()))
# z=[]
# for aa in a:
#    if aa[0]=='':
#        z.append(0)
#    elif len(aa)==1:
a,b=str(input()), str(input())
lst= [a[i:i+len(b)] for i in range(len(a))]

if b not in lst:
    print('-1')
else:
    for i in range(len(lst)):
        if b == lst[i]:
            print(i,end=' ')
# for i in range(len(string)):
#     print(string[i:i+3])
# print(lst)


# print(a)