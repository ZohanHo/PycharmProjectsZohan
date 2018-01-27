class Hots:
    gamers = "human members"
    lvl = 10
    char = "Nonane"
    nikename = "Unknown"


    def set(self, lvl, char, nickname):
        self.lvl = lvl
        self.char = char
        self.nickname = nickname

dima = Hots ()
dima.set(25, "Silvana", "Demon")
print(dima.nickname, dima.lvl, dima.char)
print(dima.char)

class Party (Hots):

    def __init__(self, weapon):
        self.weapon = weapon

vova = Party ("Bow")
vova.set (15, "Muradin", "Gorota")
print(vova.nickname, vova.weapon)
print(vova.weapon)
vova.weapon = "Dager"
#print(vova.nickname, vova.weapon)
print(vova.weapon)
