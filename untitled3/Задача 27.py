"""например я вожу 34579
и мне надо узнать суму всех цифр
мне надо єто узнать"""

a = str(34579)

f = []
for i in a:
    f.append(int(i))
    if len(f) == a.count():
        print(f)


