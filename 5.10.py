# Требуется написать программу, осуществляющую преобразование из одних единиц измерения длины в другие.
#
# Должны поддерживаться
#
#  мили (1 mile = 1609 m),
# ярды (1 yard = 0.9144 m),
# футы (1 foot = 30.48 cm),
# дюймы (1 inch = 2.54 cm),
# километры (1 km = 1000 m),
# метры (m),
# сантиметры (1 cm = 0.01 m)
# миллиметры (1 mm = 0.001 m)
# Используйте именно указанные в формулировке задачи единицы измерения с указанной точностью.
#
# Формат ввода:
# Одна строка с фразой следующего вида:
# <number> <unit_from> in <unit_to>
# например, если пришла фраза "15.5 mile in km", то требуется перевести 15.5 миль в километры.
#
# Формат вывода:
# Дробное число в научном формате (экспоненциальном), с точностью ровно два знака после запятой.
#
# Sample Input:
#
# 15.5 mile in km
# Sample Output:
#
# 2.49e+01

# https://stepik.org/lesson/21979/step/1?adaptive=true&thread=solutions&unit=5238

d={'mile':1609, 'yard': 0.9144, 'foot':0.3048,'inch':0.0254,'km':1000,'m':1,'cm':0.01,'mm':0.001}

a=input().split()
# result=(float(a[0])*d.get(a[1])/d.get(a[3]))
print("{:.2e}".format(float(a[0])*d.get(a[1])/d.get(a[3])))
# print('{:3.2e}'.format(float(a[0])*d.get(a[1])*d.get(a[3])))

# print(f'{result:.2e}')

# if a[1] in d.keys():
#     int(a[0])*d.get(a[3])
# for aa in a:
#     if aa in d.keys():
#         print(d.get(aa))
# print(a)

