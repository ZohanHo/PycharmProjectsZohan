"""Яша плавал в бассейне размером x × y метров и устал. В этот момент он обнаружил,
что находится на расстоянии x_1 метров от одного из длинных бортиков (не обязательно от ближайшего)
и y_1 метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?
Программа получает на вход числа x, y, x_1, y_1.
Программа должна вывести число метров, которое нужно проплыть Яше до бортика."""


x = 8 #int(input("Номер столбика 1(N): "))
y = 8 #int(input("Номер строки 1(M): "))

x_1 = int(input("Номер столбика 2(x_1): "))
y_1 = int(input("Номер строки 2(y_1): "))


if x_1 < y_1:
    if x_1 <= 4:
        d = (x_1 - 1 )
        print("Осталось1", d)
    if x_1 > 4:
        d =(8 - x_1)
        print("Осталось2", d)
else:
    print ("бля")






