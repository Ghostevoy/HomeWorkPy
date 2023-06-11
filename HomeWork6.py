from random import randint as rn


# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_el = int(input("Первый элемент в прогрессии: "))
delta = int(input("Разница прогрессии: "))
quantity = int(input("Количество элементов: "))
print([int(first_el + (i - 1) * delta) for i in range(1, quantity)])



# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_val = int(input("Min value: "))
max_val = int(input("Max value: "))
list_1 = [rn(1, 50) for i in range(20)]
print(list_1)
print([i for i in range(len(list_1)) if min_val < list_1[i] < max_val])
