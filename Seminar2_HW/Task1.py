# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите число монеток: '))
from random import randint
a, b = 0, 0
for i in range(n):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0: a += 1
    else: b += 1
print()
if a > b:
    print(f'Нужно перевернуть {b} монеток')
else:
    print(f'Нужно перевернуть {a} монеток')