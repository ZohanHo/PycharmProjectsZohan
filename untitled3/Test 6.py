x = {1:2, 2:3, 3:4, 4:6}
print(x.get(2,0)%x.get(5,4))

def suma (x, y):
    return x + y
print(suma(5,4))


def func(level):
    """Не могу решить"""
    if level == 1:
        return 1
    else:
        return level + func(level-1)
print(func(5))

print(func.__doc__)


