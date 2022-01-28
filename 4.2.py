# Кодирование длин серий — это базовый алгоритм сжатия данных.
#
# В этой задаче мы реализуем алгоритм дешифровки строк, закодированных с помощью одного из самых простых  вариантов кодирования длин серий.
#
# На вход алгоритму подаётся строка, содержащая цифры и символы латинского алфавита. Эта строка разбивается на так называемые "серии", которые кодируются парой число-символ или просто символ (в таком случае число считается равным единице). Результат должен содержать эти серии в том же порядке, что они и встречаются в исходной строке, при этом каждая серия раскрывается в последовательность символов соответствующей длины.
#
# Например, рассмотрим строку
#
# 3ab4c2CaB
# Разобъём её на серии
# 3a b 4c 2C a B
# После чего преобразуем серии и получим исходную закодированную строку:
# aaabccccCCaB
# Формат ввода:
# Одна строка, содержащая закодированную последовательность.
#
# Формат вывода:
# Строка, содержащая раскодированную последовательность.
#
# Sample Input:
#
# 3ab4c2CaB
# Sample Output:
#
# aaabccccCCaB

# https://stepik.org/lesson/21300/step/2?adaptive=true&unit=5101
from itertools import groupby
import re
# # string=str(input())
# # string = [string[i:i] if   for i in range(0, len(string), n)]
# # string=str(input())
# # for aa in range(len(string)):
# #     if string[aa].isdigit():
# #         print(int(string[aa])*)
# string=str(input())
# # m=len(re.sub('[1-9]', '', string))
# # print(m)
# #3a1b4c2C1a1B
# a=list(string)
# for aa in range(0,len(re.sub('[1-9]', '', string))*2,2):
#     if not a[aa].isdigit():
#         a.insert(aa,'1')
# #     print(a[aa])
# a=[int(s) if s.isdigit() else s for s in a]
# for aa in range(0,len(a),2):
#     print(a[aa]*a[aa+1],end='')
# for aa in a:
#     if aa.isdigit():
#         aa=int(aa)
# print(a)
# ['AAA', 'T', 'GG']

# s='3ab4c2CaB'
# l = [x.split('_')[1] for x in s.split(', ') if x.isdigit()]
# print(l)
# string=str(input())
# def one(string):
#     for aa in range(len(string)):
#         if
# print(a[0]*a[1])
# print(len(a))

string=str(input())
m=re.split('(\d+)',string)
s=[]
for mm in m:
    if mm.isdigit() or len(mm)==1:
        s.append([mm])
    else: s.append(list(mm))
s=[item for sublist in s for item in sublist]
for ss in range(0,len(re.sub('[0-9]', '', string))*2,2):
    if not s[ss].isdigit():
            s.insert(ss,'1')
s=[int(s) if s.isdigit() else s for s in s]
for aa in range(0,len(s),2):
    print(s[aa]*s[aa+1],end='')



# v2:
# string=str(input())
# m=re.split(r'\d{0,4}[A-Za-z]{1}',string)
# print(m)

#
# for aa in range(0,len(re.sub('[1-9]', '', s))*2,2):
#     if not s[aa].isdigit():
#         s.insert(aa,'1')
# print(s)
# m=[j for i in m for j in i]
# print(m)
# if not string[0].isdigit():
#     string='1'+string
# print(string)
#
# for a in range(len(string)):
#     if not (string[a] and string[a+1]).isdigit():
#         string=string[:string[a]]+'1'+string[string[a]:]
# print(string)