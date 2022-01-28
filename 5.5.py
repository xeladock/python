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
# Формат ввода:
# Строка, содержащая натуральное число nn, 0 < n < 40000<n<4000.
#
# Формат вывода:
# Строка, содержащая число, закодированное в римской системе счисления.
#
# Sample Input 1:
#
# 1984
# Sample Output 1:
#
# MCMLXXXIV
# Sample Input 2:
#
# 9
# Sample Output 2:
#
# IX
# Sample Input 3:
#
# 3
# Sample Output 3:
#
# III

# https://stepik.org/lesson/21633/step/1?adaptive=true&thread=solutions&unit=5133

# d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# a=str(input())
# lst=[a[i:i+2] for i in range(len(a))]
# print(lst)
def nearest(lst, target):
    return max([i for i in lst if i <= target])

d={5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM',1:'I'}
a=list(reversed([int(a) for a in str(input())]))

# if len(a)==1 and a[0]<4:
#     print(a[0]*'I')
#     exit()

# print(a)
c=[]
for i in range(len(a))[::-1]:
    # if a[i]==0:a[i]=1
    n=a[i]*(10**i)
    print(n)
    if n==0:continue
    if n in d.keys():
        c.append(d.get(n))
    else:
        g=0
        while n != 0:
            if g==n:c.append(d.get(n));break
            g=nearest(d.keys(),n)
        # c.append(d.get(nearest(d.keys(),n)))
        #
            c.append(d.get(g))

            n=n-g
print(''.join(str(e) for e in c))




        # u=0
        # while n!=0:
        #     g=nearest(d.keys(),n)
        # c.append(d.get(nearest(d.keys(),n)))

            # c.append(d.get(g)*(n//g))
            #
            # n=n-g
            # u+=1
        # print('this'+str(g))

        # for i in d.keys():
        #     if ((n//i==1) and (n!=i)):
        #         c.append(d.get(i))
        #         c.append(n % i)
            # else:
            #     aa = [int(a) for a in str(n%i)]
            #     if len(aa) == 1:
            #         c.append(aa[0] * 'I')
            #     if len(aa) == 2:
            #         c.append(aa[0] * 'X')
            #     if len(aa) == 3:
            #         c.append(aa[0] * 'C')
            #     if len(aa) == 4:
            #         c.append(aa[0] * 'M')
                # c.append(n%i)
                # break
#             # else:
#                 # aa = [int(a) for a in str(n % i)]
#                 # c.append(aa[0] * 'I')
# print(c)

# for i in c:
#     if isinstance(i,int):
#         aa=[int(a) for a in str(i)]
#         if len(aa)==1:
#             print(aa[0]*'I')
#         if len(aa)==2:
#             print(aa[0]*'X')
#         if len(aa)==3:
#             print(aa[0]*'C')

    # print(i if isinstance(i,int) else '',end='')



# print(a)

# for i,j in enumerate(a):
#     print(reversed(j),i)
