"""Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!.
Пользоваться математической библиотекой math в этой задаче запрещено."""

n = int(input("введите факториал какого числа необходимо вычислить: "))

s = [i for i in range(1, n + 1)]
for j in range(len(s)):
    s[j] = s[j] * (len(s) + 1)
    print(s)












#



