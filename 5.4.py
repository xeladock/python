# В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):
#
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.
#
# Напишите программу, которая переводит число из римской в десятичную систему счисления.
#
# Формат ввода:
# Строка, содержащая число, закодированное в римской системе счисления. Гарантируется, что число меньше 4000.
#
# Формат вывода:
# Строка, содержащая число в десятичной системе счисления, соответствующее введённому.
#
# Sample Input 1:
#
# MCMLXXXIV
# Sample Output 1:
#
# 1984
# Sample Input 2:
#
# IX
# Sample Output 2:
#
# 9
# Sample Input 3:
#
# III
# Sample Output 3:
#
# 3

# https://stepik.org/lesson/21443/step/1?adaptive=true&thread=solutions&unit=5116

d={5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',1:'I'}

a=input()
g=a
# b=['IV','IX','XL','XC','CD','CM']
# lst= [a[i:i+2] for i in range(len(a))]
# lst=list(a)
res=[]
# lst.extend(b)

for i in range(len(a)):

    try:
            s = a[i] + a[i + 1]
            if a[i]+a[i+1] in d.values():

                res.append(list(d.keys())[list(d.values()).index(a[i]+a[i+1])])
                g=g.replace(a[i]+a[i+1],'')
        # print(a[i]+a[i+1])
    except:
        break

for i in g:
    # if len(g)==0: break
    if i in d.values():
        res.append(list(d.keys())[list(d.values()).index(i)])
print(sum(res))
# print(g)

# lst.extend(lst2)
# lst=set(lst)
# lst=set(lst)
# print(lst)
# for s in lst:
#     if s in d.values():
#         print(list(d.keys())[list(d.values()).index(s)])


# print(lst)
# for i in lst:
#     print(list(d.keys())[list(d.values()).index(i)])


# print(lst)
# print(lst2)