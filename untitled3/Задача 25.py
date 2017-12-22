"""По данному натуральному n вычислите сумму 13+23+33+...+n3."""

n = int(input("введите количество чисел: "))

spisok = []

for i in list(range(1, n+1)):
    s = (i ** 3)
    spisok.append(int(s))
    if len(spisok) == n:
        print(sum(spisok))

