i = 0

while i < 4:
    i += 1
    print(i)
    if  i == 2:
        print("двойка")
        continue
    print("Что то")



for n in 'hello world':
    if n == 'o':
        continue
    print(n, end ="", sep=":")



for j in list(range(10)):
    if not j % 2 == 0:
        continue
    print(j, end="")
