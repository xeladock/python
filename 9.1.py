# A durak deck contains 36 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S). Each card also has a value of either 6 through 10, jack, queen, king, or ace (denoted 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 6 having the lowest and ace the highest value.
#
# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
#
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>, а на следующей строке указывается козырная масть.
#
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.
#
# Sample Input 1:
#
# AH JH
# D
# Sample Output 1:
#
# First
# Sample Input 2:
#
# AH JS
# S
# Sample Output 2:
#
# Second
# Sample Input 3:
#
# 7C 10H
# S
# Sample Output 3:
#
# Error
# https://stepik.org/lesson/22985/step/1?adaptive=true&thread=solutions&unit=5369
import re
import time
start_time = time.time()
# print('A'>'1J')
# print('1J'>'1K')
# print('6'>'5')
# a=[str(x) for x in input().split()]
# a=[item for sublist in a for item in sublist]
a=str(input())
''.join(a.split())
for aa in a:
    # print(aa)
    # # print(a[aa])
    if aa=='J':
        a=a.replace(aa,'11')
        break
        # a.remove(a[aa+1])
    elif aa == 'Q':
        a=a.replace(aa, '12')
        break
        # a.remove(a[aa + 1])
    elif aa=='K':
        a=a.replace(aa,'13')
        break
        # a.remove(a[aa+1])
    elif aa=='A':
        a=a.replace(aa,'14')
        break
        # a.remove(a[aa+1])
# a=re.split(r"([a-z]+)([0-9]+)", a)
a=re.split('(\d+)',a)[1:]
# print(a)
# # c=[item for sublist in c for item in sublist]
# print(c)
# # print(a)
b=str(input())
a=[int(s) if s.isdigit() else s for s in a]
print(a)
print(a[1])
print(a[3])
if a[1]==a[3]:
    print("First" if a[0]>a[2] else "Second")
    exit()
if  b == a[1]:
    print('First')
    exit()
if  b == a[3]:
    print('Second')
    exit()
print('Error')
print ("time elapsed: {:.2f}s".format(time.time() - start_time))
# if (b in a):
#     print('First' if a[0]>a[2] else 'Second')
#     exit()
# if ((b not in a) and (a[1]!=a[3])):
#     print('Error')
#     exit()
# #
# # if 'J' in a:
# #     a.index('J')=='1J'
# # b=str(input())
# print('First' if a[0]>a[2] else 'Second')
# print(b)


