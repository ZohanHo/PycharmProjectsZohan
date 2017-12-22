def func(n):
    y = '*'.join(str(x) for x in range (1, n, 2))  #Функция eval умноажет все елементы цыкла for, 1*3*5 = 15б join добавляет умножение в итерацию, после такта
    return eval(y)
print(func(7))


