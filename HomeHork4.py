import random


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

len_list1 = int(input("Длина первого набора чисел: "))
len_list2 = int(input("Длина второго набора чисел: "))
list1 = []
list2 = []
result = []

for i in range(len_list1):
    list1.append(int(input(f"Введи {i+1} элемент первого набора: ")))
for j in range(len_list2):
    list2.append(int(input(f"Введи {j+1} элемент второго набора: ")))

print(list1)
print(list2)

for el in list1:
    if el in list2:
        result.append(el)

result.sort()
resSet = set(result)
print(resSet)



#
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


bush = int(input("Сколько кустов??????? "))

berries = {}
result = []
for i in range(bush):
    berries[i] = random.randint(1, 20)

for k in berries:
    if k == 0:
        result.append(berries[len(berries)-1] + berries[0] + berries[1])
    elif k == len(berries) - 1:
        result.append(berries[0] + berries[k-1] + berries[k])
    else:
        result.append(berries[k-1] + berries[k] + berries[k+1])


maxIndex = 0
for j in range(len(result)):
    if result[maxIndex] < result[j]:
        maxIndex = j

print(result)
if maxIndex != 0 or maxIndex !=len(berries)-1:
    print(f'Больше всего ягод будет собрано, если начать с куста {maxIndex + 1}. Получится собрать {result[maxIndex]+result[maxIndex+1] + result[maxIndex-1]}')
elif maxIndex == 0:
    print(f'Больше всего ягод будет собрано, если начать с куста {maxIndex + 1}. Получится собрать {result[maxIndex] + result[maxIndex + 1] + result[1]}')
else:
    print(f'Больше всего ягод будет собрано, если начать с куста {maxIndex + 1}. Получится собрать {result[maxIndex] + result[0] + result[maxIndex - 1]}')
