# #num = input("Введите число ")

# num = int(input("Введите число "))
# # i = 0 
# # while i <= num: 
# #     print(f"квадрат числа {i} равен {i**2} ")
# #     i += 1
# for i in range(num + 1):
#     print(f"квадрат числа {i} равен {i**2} ")
#     if i % 2 == 1:
#         print("Нечетное")
#     elif i % 3 == 0:
#         print("Делится на три")

# Задача 1:
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input("1: "))
m = int(input("Введите 2 число: "))
d = int((m - 1 + n) / n)
print(d)
