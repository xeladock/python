# Напишите простой интерпретатор математического выражения.
#
# На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a \texttt{ operator } ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.
#
# Формат ввода:
# Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.
#
# Формат вывода:
# Строка, содержащая целое число -− результат вычисления.
#
# Sample Input 1:
#
# 45 plus 8
# Sample Output 1:
#
# 53
# Sample Input 2:
#
# 12 minus 42
# Sample Output 2:
#
# -30
# Sample Input 3:
#
# 451 multiply 2
# Sample Output 3:
#
# 902
# Sample Input 4:
#
# 13 divide 3
# Sample Output 4:
#
# 4

# https://stepik.org/lesson/22243/step/1?adaptive=true&thread=solutions&unit=5316

a = [str(x) for x in input().split()]
if a[1] == 'plus':
    print(int(a[0]) + int(a[2]))
if a[1] == 'minus':
    print(int(a[0]) - int(a[2]))
if a[1] == 'multiply':
    print(int(a[0]) * int(a[2]))
if a[1] == 'divide':
    print(int(a[0]) // int(a[2]))


