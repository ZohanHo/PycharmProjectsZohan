"""Последовательность состоит из натуральных чисел и завершается числом 0.
Определите индекс наибольшего элемента последовательности.
 Если наибольших элементов несколько, выведите индекс первого из них.
  Нумерация элементов начинается с нуля."""

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

print(s)