"""Определите среднее значение всех элементов последовательности, завершающейся числом 0."""

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
x = (sum(k) / (len(k)-1))
print(x)