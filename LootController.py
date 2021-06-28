import random



class Loot:
    def __init__(self):
        pass


    class TestWep():

        name = 'Cool Weapon'
        level = 1
        dmg = 5
    class TestWep2():
        name = 'Taco'
        level = 2
        dmg = 7

    class TestArmor():
        name = 'Armor'
        level = 1
        dmg = 2

    armorList = [TestArmor]
    wepList = [TestWep, TestWep2]
    lootList = [armorList, wepList]


    def loot_drop_roll(self):


        i = random.randint(0, (len(Loot.lootList) - 1))
        if i == 0:
            x = Loot.armorList
            b = random.randint(0, (len(x)-1))
            self.ldr = Loot.armorList[b]
        elif i == 1:
            x = Loot.wepList
            b = random.randint(0, (len(x)-1))
            self.ldr = Loot.wepList[b]
        else:
            pass


#Calls Loot drop roll
Loot.loot_drop_roll(Loot)


print (Loot.ldr.name)
print (Loot.ldr.level)
print (Loot.ldr.dmg)
