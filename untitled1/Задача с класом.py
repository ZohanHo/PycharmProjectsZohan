class C:
    def __init__(self):
        self.int = 2
    def __add__(self, other):
        return self.int + other.int
a = C()
b = C()
print (str(a+b))
