# Выведите таблицу размером n \times nn×n, заполненную целыми числами от 11 до n^2n
# 2
#   по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.
#
# Формат ввода:
# Одна строка, содержащая одно целое число nn, n > 0n>0.
#
# Формат вывода:
# Таблица из nn строк, значения в строках разделены пробелом.
#
# Sample Input:
#
# 5
# Sample Output:
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

# https://stepik.org/lesson/21976/step/2?adaptive=true&unit=5236

# aa=int(input())
# a=[int(i) for i in range (1,aa**2+1)]
# a=[a[i:i + aa] for i in range(0, len(a), aa)]
# matrix = [ [ 0 for i in range(aa) ] for j in range(aa) ]
# n=0
# m=aa
# while n!=len(matrix):
#     matrix[n]=a[n]
#     n=n+1
#     for i in range(n-1,m-1):
#             matrix[i+1][-1]=a[n][i]
#     for i in range()
# print(matrix)

aa=int(input())
matrix = [ [ 0 for i in range(aa) ] for j in range(aa) ]
res=[];s=0
while s!=aa**2:
    i=0;j=0;k=0
    while j!=len(matrix[0]):
        s+=1
        matrix[i][j]=s
        j+=1
    j = 1
    while k!=len(matrix[0])-1:
        s += 1
        matrix[j][-1]=s
        j+=1; k+=1
    k=0; j=-2
    while k!=len(matrix[0])-1:
        s+=1
        matrix[-1][j]=s
        j-=1; k+=1
    k=0; i=-2
    if len(matrix[0])==1:
        matrix[0][0]=aa**2
    else:
        while k!=len(matrix[0])-2:
            s+=1
            matrix[i][0]=s
            i-=1; k+=1
    if len(matrix)==aa:
        res.extend(matrix)
    gg=len(matrix)-2
    if len(matrix)!=aa:
        while len(matrix[0])!=len(res[0]):
            for ii in range(0, len(matrix)):
                matrix[ii].append(0); matrix[ii].insert(0,0)
        while len(matrix)!=len(res):
                matrix.append([0 for i in range(aa)]); matrix.insert(0,[0 for i in range(aa)])
        tmp=[]
        for i in range(aa):
                tmp.append([a1 + b1 for a1, b1 in zip(matrix[i], res[i])])
        res.clear();res.extend(tmp)
    matrix = [[0 for i in range(gg)] for j in range(gg)]
for i in res: print(*i)





# k=0
# ss=[]
# s=0
# while s!=aa**2:
#     i=0;j=0;k=0
#     while j!=len(matrix[0]):
#         s+=1
#         matrix[i][j]=s
#         j+=1
#     i+=1
#     while 0 in matrix[i]:
#         s += 1
#         matrix[i][j-1]=s
#         i+=1
#         if s==(aa*2)-1:
#             i=i-(aa+1)
#             j=j-(aa+2)
#             while 0 in matrix[i]:
#                 s+=1
#                 matrix[i][j]=s
#                 j-=1
#
#     j+=1
#     k+=1
#     while k!=(aa-1):
#         i -= 1
#         s+=1
#         matrix[i][j]=s
#         k+=1
#     # s.extend(matrix)
#     ss.extend(matrix)
#     matrix = [[0 for i in range(matrix[1].count(0))] for j in range(matrix[1].count(0))]
#
#
# print(ss)
# print(matrix)

# matrix[0]=matrix0[0]
# --------
# print(matrix)
# x=(aa*2)+aa-2
# y=x+(aa-2)
# print(y)
# for i in range(aa):
#     matrix[0][i]=i+1
#     matrix[1][i]=y+i
#     matrix[-1][i]=x-i
#
#     # print(matrix[-1][-1 - i])
#
# for i in range(1,aa-1):
#     matrix[i][-1]=aa+i
#     matrix[aa-(i+1)][0]=x+i
#     while i!=aa-2:
#         matrix[i+1][-2]=matrix[1][-2]+i
#         break
#     if i==aa-2:
#         i =-3
#         while 0 in matrix[-2]:
#             matrix[-2][i]=matrix[-2][i+1]+1
#             i-=1
#     #     matrix[-2][]
#     # matrix[][2]
# print(matrix)
# ---------
# for i in range(aa-2):

#
# print(x)
# print(matrix)

# m=[]
# for i in range(a):

# m.append(matrix0[0])
# i=0
# d=1
# while True:
#     s=aa+(aa-d)
#     for g in range(s,s+(aa-d)):
#         print(g)
            # mm=[]
            # mm.append(aa[g])
# print(m)
# print(matrix)
# while s!=aa*2:
#    while s!=aa:
#        for i in a:
#         mm.append(i)
#     m.append(mm)

# hor=vert=click=0
# left=right=up=down=click=0
# while True:
#     while 0 in matrix[left]:
#         for i in a:
#             matrix[left][click]=i
#             click+=1
#             if i+1%aa==0:
#                 click=0
#                 break
#         down+=1
#         iter=1
#         for i in a:
#             matrix[down][click-iter]=i
#             down+=1
#             if down == aa-iter:
#                 break

