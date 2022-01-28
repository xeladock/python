# Задача на работу со строками.
#
# Многим знакома детская загадка:
#
# А и Б сидели на трубе.
# А упало, Б пропало.
# Что осталось на трубе?
#
# Перевод, (какой я смог найти):
#
# A and B sat in the tree.
# A had fallen, B was stolen.
# What's remaining in the tree?
#
# Напишите программу, которая считывает два имени и выводит стихотворение, в котором вместо A и B используются эти имена.
#
# Формат ввода:
# Два имени, разделённых переносом строки. Первое имя должно заменять A, второе -− B.
#
# Формат вывода:
# Три строки стихотворения с заменёнными A и B.
#
# Sample Input:
#
# X
# Y
# Sample Output:
#
# X and Y sat in the tree.
# X had fallen, Y was stolen.
# What's remaining in the tree?

# https://stepik.org/lesson/22772/step/2?adaptive=true&unit=5346

string="A and B sat in the tree.\nA had fallen, B was stolen.\nWhat's remaining in the tree?"

a, b=str(input()), str(input())
print(f"{a} and {b} sat in the tree.\n{a} had fallen, {b} was stolen.\n"
      f"What's remaining in the tree?")
# string=string.replace('A',a)
# string=string.replace('B',b)
# print(string)
# print()
# str.replace('A', a)
# print(string)
