s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение этих чисел: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, y)