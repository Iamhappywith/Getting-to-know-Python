# Задача №25. Общее обсуждение
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

 #25
string = "a a a b c a a d c d d"
dict = {}
for i in string.split(" "):
    dict[i] = 0
for i in string.split(" "):
    dict[i] += 1
res = ""
string = string[::-1]
for i in string.split(" "):
    if (dict[i] == 0):
        res += i + " "
    res += i + "_"+str(dict[i]-1) + " "
    dict[i] -= 1
res = " ".join(res.split(" ")[::-1])
res = res.replace("_0","")
print(res)