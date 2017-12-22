# Процедуры и функции, что таоке вернуть значение


def surname (name):

    """ В большинстве своем любая программа сосотоит из более мелких подпрограмм. Каждая подпрограмма выполняет
определенное законченое действие (что-то считает, рисует, считывает из файла (памяти) или пишет в файл (память) и т.п.)
Так вот есть два вида подпрограмм - процедура (procedure) и функция (function).

Разница между ними следующая:

Процедура выполняет часть программы (подпрограмму) и затем переходит к следующему
участку программы.

Функция делает тоже самое, и после окончания подпрограммы также переходит к следующему участку всей программы но перед
этим записывает в память результат выполнения функции.

Это и есть понятие "возвращает значение". Само значение (тип его - число, строка, изображение
и т.п) указывается при первом описании функции. При этом использование возвращаемого значения функции необязательно.

Сам программист определяет это программно. Удобство применения функции в том, что ее можно использовать в качестве
аргумента в операторе языка или как аргумент другой подпрограммы."""

    d = {"Иван" : "Иванов" , "Василий" : "Петров" , "Николай" : "Клонов"}
    return d[name]

surnames = surname("Николай")

print(surnames)

print (surname.__doc__)