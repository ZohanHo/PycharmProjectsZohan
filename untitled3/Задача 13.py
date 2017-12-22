"""Даны три целых числа. Выведите значение наименьшего из них."""


x = int(input("Введите число x: "))
y = int(input("Введите число y: "))
z = int(input("Введите число z: "))

if x < (y and z):
    print("x меньее")
elif y < (x and z):
    print("y меньее")
elif z < (x and y):
    print("z меньее")


