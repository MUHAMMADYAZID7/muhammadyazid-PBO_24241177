class Hero:
    
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        self.__private = 'private'
        self.protected = 'protected'

hero_1 = Hero('Atsu',100)

print(hero_1.__dict__)
print(Hero.__dict__)
print(Hero.__private_Jumlah)