"""Определите сумму всех элементов последовательности, завершающейся числом 0.
 В этой и во всех следующих задачах числа, следующие за первым нулем,
 учитывать не нужно."""

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
print(sum(k))
