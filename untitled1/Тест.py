class super:
    ears  = 36             #в класах переменные наз - оплями
    name = "Evgen"
    lastname = "Serduk"
    stage = 11

    def set(self, ears, name, lastname):             #В класах функции наз - методами
        self.ears = ears                      #self - обязательный оргумент который содержит метод класа, передащщейся при вызове метода
        self.name = name                      #Через self обращаемся уже к переменнной, в данном случае name
        self.lastname =lastname

new1 = super()          #new1 обьект класса super
print (new1.name)       #через обьект обращаемся к свойствам класа, а именно к имени и вывожу

new2 = super()
new2.lastname = "Сердюк"  #переназначил фамили по руский для обьекта new2
print (new2.lastname)

new3 = super()
new3.ears = 37            #переназначил возраст для обьекта new3, и вывел
print (new3.ears)

new4 = super()
new4.set(str(40), "funny", "funk")         #Передаю через функцию новые поля класа (свойства)
print (new4.name + " " + new4.lastname + " " + str(new4.ears))  #вывожу новые поля класа



