# Напишите
# функцию
# f(x)
# f(x), принимающую
# дробное
# число
# xx
# и
# возвращающую
# значение
# следующей
# функции, определённой
# на
# всей
# числовой
# прямой:  
#
# f(x) = \begin
# {cases}
# 1 - (x + 2) ^ 2,\quad &\text
# {при}
# x\le - 2\\  -\frac
# x2,\quad &\text
# {при} - 2 \lt
# x \le
# 2\\   (x - 2) ^ 2 + 1,\quad &\text
# {при}
# 2 \lt
# x \end
# {cases}
# f(x) =
# ⎩
# ⎨
# ⎧
# ​
#
# 1−(x + 2)
# 2
# ,
# −
# 2
# x
# ​
# ,
# (x−2)
# 2
# +1,
# ​
#
# при
# x≤−2
# при −2 < x≤2
# при
# 2 < x
# ​
#
# Требуется
# реализовать
# только
# функцию, решение
# не
# должно
# осуществлять
# операций
# ввода - вывода.
#
# Sample
# Input
# 1:
#
# 4.5
# Sample
# Output
# 1:
#
# 7.25
# Sample
# Input
# 2:
#
# -4.5
# Sample
# Output
# 2:
#
# -5.25
# Sample
# Input
# 3:
#
# 1.0
# Sample
# Output
# 3:
#
# -0.5

#https://stepik.org/lesson/21208/step/2?adaptive=true&unit=5094

def f(x):
    if x<=-2:
        return(1-((x+2)**2))
    elif -2<x<=2:
        return(-(x/2))
    else:
        return((x-2)**2)+1

a=float(input())

print(f(a))
