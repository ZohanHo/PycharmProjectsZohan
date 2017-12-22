try:
    a,b = "hello",0
    c = a/b
except TypeError:  #Сработает TypeEroor, а любое число в нулевой ето 1
    print(2**0)
except DivisionByZeroError: #Ошибка прописана неверно
    print(2**1)


