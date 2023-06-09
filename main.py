# import random
#
#
#Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

head = 0
tail = 0
num_coin = int(input("Введи количество монеток: "))
coin = []

for i in range(num_coin):
    coin.append(random.randint(0, 1))
print(coin)

for j in coin:
    if j == 1:
        head += 1
    else:
        tail += 1

if head == len(coin) or tail == len(coin):
    print("Все монетки повернуты одной стороной.")
elif head > tail:
    print(f'Необходимо перевернуть {tail}.')
else: print(f"Необходимо перевернуть {head}.")


#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


amount_num = int(input("Сумма загаданных чисел: "))
mult_num = int(input("Произведение загаданных чисел: "))
search_complete = False

for i in range(1000):
    if search_complete == True:
        break
    for j in range(1000):
        if i+j == amount_num and i*j == mult_num:
            print(f"Под условия подходят числа {i} и {j}")
            search_complete = True
            break



#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

n = int(input("Введи число: "))
rank = 0

while 2**rank < n:
    print(2**rank, end= " ")
    rank+=1