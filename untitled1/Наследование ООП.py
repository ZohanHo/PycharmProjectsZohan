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
print (new1.name)

class nova(super):
    basket = "Basket profi"
    volik = "Superprofi"
    sportstage = 15


sport = nova()
print(sport.lastname + "  " + sport.volik)

class supernova (nova):
    moroz = 3500

dolg = supernova()
print(int(dolg.stage) + int(dolg.moroz) + int(dolg.sportstage))

print(super.ears)
print(new1.ears)

print(dolg.moroz)          #Выводить значение moroz модено как через название так и через название обьекта класа
print(supernova.moroz)






"""class bdo:

    kzarka = 1
    karanda = 1
    dreven = 0

    def set2(self, kzarka, karanda,dreven):
        self.kzarka = kzarka
        self.karanda = karanda
        self.dreven = dreven

tantum = bdo()
tantum.dreven = 1
print(int (tantum.kzarka) + int(tantum.karanda) + int(tantum.dreven))"""


