"""По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!.
В решении этой задачи можно использовать только один цикл.
Пользоваться математической библиотекой math в этой задаче запрещено."""

n = int(input("введите факториал какого числа необходимо вычислить: "))

s = 1
for i in range(1, n + 1 ):
    s = s * i
    if (i) == n:
        print(s)

