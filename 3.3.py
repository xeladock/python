# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Также функция не должна осуществлять ввод/вывод информации.
# https://stepik.org/lesson/21209/step/2?adaptive=true&unit=5095


lst = [1, 2, 3, 4, 5, 6]


def modify_list(lst):
    m = []
    for l in lst:
        if l % 2 == 0:
            m.append(l // 2)
    lst.clear();
    lst.extend(m)
    return m


# def modify_list(numbers):
#     numbers[:] = [i//2 for i in numbers if i%2 == 0]