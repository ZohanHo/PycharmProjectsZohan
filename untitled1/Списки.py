a = ["Nova", 4, 45.3, 5, 6, "Koloss"]

a.pop(1)  #Удаляет элемент по индексу
print(a)

a.remove(45.3)  #удаляет конкретный элемент по имени
print(a)

a.append("super")  #Добавляет элемент в конец списка
print(a)

a.index(5)
print(a.index(5))  #выводит индекс обьекта в списке


a.pop(a.index(6))  #Индекс 6 ето 4, соответственно ето 6, он удаляется
print(a)



def nova(x):
    return x * 2           #вернуть когда не нужно выводить, а нужно присвоить переменной

newnova = nova(5)
print(newnova)

def nova(x):
    print (x * 2)           #выводим сразу значение
nova(5)



def func(a, b, c = 2):
    return a+b+c                 #возвращает и не выодит, но присвоев вызов функции переменной, мы можем ее вывести, и получить результат
r = func(2, 3)
print(r)

def slovar(**slovar):
    print (slovar)
slovar()





