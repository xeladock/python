# Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в множество объединённых интервалов \{-10\} \cup (-5, 3] \cup (8, 12) \cup [16, +\infty){−10}∪(−5,3]∪(8,12)∪[16,+∞) и False в противном случае.
# #
# # Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии.
# #
# # Формат ввода:
# # Строка, содержащая целое число.
# #
# # Формат вывода:
# # True или False.
# #
# # Sample Input:
# #
# # 20
# # Sample Output:
# #
# # True
# https://stepik.org/lesson/22425/step/1?adaptive=true&thread=solutions&unit=5336
x=int(input())
print('True' if (x==-10) or (-5>x>=3) or (12>x>8) or (x>=16) else 'False' )
