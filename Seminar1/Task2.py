# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

k1 = int(input("Введите сколько учеников в 1 классе ")) 
k2 = int(input("Введите сколько учеников во 2 классе ")) 
k3 = int(input("Введите сколько учеников в 3 классе ")) 
i = 2 
p1 = (k1 // 2) + (k1 % i)
p2 = (k2 // 2) + (k2 % i)
p3 = (k3 // 2) + (k3 % i)
print(p1 + p2 + p3)