"""Последовательность состоит из натуральных чисел и завершается числом 0.
 Определите, сколько элементов этой последовательности равны ее наибольшему элементу."""

n = int(input("введите число повторений n: "))

r = []
i = 0
while i in range(n):
    k = int(input("введите число k: "))
    r.append(k)
    i += 1

k = []
for j in list(r):
    k.append(j)
    if j == 0:
        break
d = max(k)

s = []
for x in k:
    if x == d:
        s.append(x)

print(len(s))