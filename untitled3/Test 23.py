def func(x):
    """Функция обязательная для повторения !!!"""
    res = 0
    for i in range(x):  # Итерация проходит так: i = 0, 0 находится в диапазоне до 4. значит res = 0 + 0, делее i = 1, res = 0 + 1
        res += i
    return res

print(func(4))


print(func.__doc__)