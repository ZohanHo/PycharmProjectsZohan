"""Последовательность состоит из различных натуральных чисел и завершается числом 0.
 Определите значение второго по величине элемента в этой последовательности.
 Гарантируется, что в последовательности есть хотя бы два элемента."""

n = int(input("введите число повторений n: "))

r = []
for i in range(n):
    k = int(input("введите число k: "))
    r.append(k)
k = []
for j in list(r):
    k.append(j)

    if j == 0:
        break
x = (max(k))
s = (k.index(x))
k.pop(s)
print(max(k))