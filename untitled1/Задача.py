def func (x):
    x[0] = ["def"]
    x[1] = ["abc"]
    return id(x)
q = ["abc", "def"]
print(id(q) == func(q))
