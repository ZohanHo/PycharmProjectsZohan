"""Шахматная ладья ходит по горизонтали или вертикали. Даны две различные клетки шахматной доски,
определите, может ли ладья попасть с первой клетки на вторую одним ходом.
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки,
потом для второй клетки. Программа должна вывести YES,
если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае."""

x = int(input("Номер столбика 1: "))
y = int(input("Номер строки 1: "))

x_1 = int(input("Номер столбика 2: "))
y_1 = int(input("Номер строки 2: "))


if x == x_1:
    print("Может")
elif y == y_1:
    print("Может")
else:
    print("Не может")


