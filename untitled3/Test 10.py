n = int(input("Введите: "))

i = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    print(n)
    i += 1
print(i)
