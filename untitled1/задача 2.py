def fun():
    for x in range(8):
        yield (x)
x = fun()
for a in range (7):
    next(x)
print(next(x))




test = iter([1, 2, 3, 4, 5])
print ([x for x in test])

