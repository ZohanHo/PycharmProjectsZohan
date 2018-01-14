def fun(x):
    def add(y):
        return x + y
    return add
v = fun(100)
print(v(200))



