"""Определите количество четных элементов в последовательности, завершающейся числом 0."""

n = int(input("введите число повторений n: "))

r = []
for i in range(n):
    k = int(input("введите число k: "))
    r.append(k)
k = []
for j in list(r):
    if j % 2 == 0:
        k.append(j)

        if j == 0:
            break

print(len(k)-1)