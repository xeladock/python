# /*Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.
#
# Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.
#
# Формат ввода:
#
# Два слова, каждое на отдельной строке.
# Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.
#
# Формат вывода:
# True или False.
# https://stepik.org/lesson/22966/step/1?adaptive=true&unit=5367


# a=set(list(str(input().lower())))
# b=str(input().lower())
# # for bb in b:
#
# # print(a)
# # print(b)
# for bb in b:
#     if bb in a:
#         continue
#     else: print("False"); exit()
# print("True")

# print(b[::-1])
a=sorted(list(str(input().lower())))
b=sorted(list(str(input().lower())))
print('True' if a==b else 'False')
