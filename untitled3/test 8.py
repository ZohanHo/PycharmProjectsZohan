class Hots:
    klan = "Slayr"      #Переменный в класе называюся полями
    group = "noob"

    def set(self, klan, group):
        self.klan = klan
        self.group = group

gesilion = Hots()         #Слава обьект класа Хотс
gesilion.uron = 200
gesilion.set ("Drago", "Supernoob")
print(gesilion.klan, gesilion.group)


nasar = Hots()         #Назар обьект класа Хотс
s = nasar.group = 380
nasar.set("Body", "Prime")
print("Клан назара" , nasar.klan)


print(s)

print("Урон гесилиона : " , gesilion.uron)
