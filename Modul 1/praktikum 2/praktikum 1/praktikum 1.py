class Hero: 
    pass

hero_1 = Hero() 
hero_2 = Hero() 

hero_1.name = "lilla"
hero_2.name = "adi"

hero_1.power = 100
hero_2.power = 10


print(hero_1.name)
print(hero_2.name)  
print(hero_1.__dict__) 