# Шифр Цезаря заключается в замене каждого символа входной строки на символ, находящийся на несколько позиций левее или правее его в алфавите.
#
# Для всех символов сдвиг один и тот же. Сдвиг циклический, т.е. если к последнему символу алфавита применить единичный сдвиг, то он заменится на первый символ, и наоборот.
#
# Напишите программу, которая шифрует текст шифром Цезаря.
#
# Используемый алфавит -− пробел и малые символы латинского алфавита: ' abcdefghijklmnopqrstuvwxyz'
#
# Формат ввода:
# На первой строке указывается используемый сдвиг шифрования: целое число. Положительное число соответствует сдвигу вправо. На второй строке указывается непустая фраза для шифрования. Ведущие и завершающие пробелы не учитывать.
#
# Формат вывода:
# Единственная строка, в которой записана фраза: Result: "..." , где вместо многоточия внутри кавычек записана зашифрованная последовательность.
#
# Sample Input 1:
#
# 3
# i am caesar
# Sample Output 1:
#
# Result: "lcdpcfdhvdu"
# Sample Input 2:
#
# -2
# az
# Sample Output 2:
#
# Result: "zx"
# Sample Input 3:
#
# 27
# abc
# Sample Output 3:
#
# Result: "abc"
#i am caesar
# a=' abcdefghijklmnopqrstuvwxyz'
import itertools
a=' abcdefghijklmnopqrstuvwxyz'
# print(a)
c=int(input())
b = str(input().strip())
print(b)
n=0
res=''
# while n!=len(b):
for text in b:
        res=res+a[(a.index(text)+c)%27]
        # n+=1
        # if n==len(b):
print('Result: {}'.format(res))
            # exit()
# print(b.index('i'))
# print(b[a.index('i')])
# print(a[9])
# c=int(input())
# d=
# # string=''
# # # print(a[-1])
# # n=0
# for text in itertools.cycle(range(len(a))):
#     for text2 in range(len(b)):






#     while n!=len(b):
#         print(a[b[text+c]])
#         n=n+1
#         break
    # n=n+1
    # if n==10: exit()

