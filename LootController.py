import random



class Loot:
    def __init__(self):
        pass

    ldr = []
    drops = []
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
    #Loot drop lists
    armorList = [TestArmor]
    wepList = [TestWep, TestWep2]
    lootList = [armorList, wepList]

    #Get loot that was dropped
    def loot_drop_roll(self):
        self.drops = []

        i = random.randint(0, (len(Loot.lootList) - 1))
        if i == 0:
            x = Loot.armorList
            b = random.randint(0, (len(x)-1))
            self.drops.append(Loot.armorList[b])
            self.ldr.append(Loot.armorList[b])
        elif i == 1:
            x = Loot.wepList
            b = random.randint(0, (len(x)-1))
            self.drops.append(Loot.wepList[b])
            self.ldr.append(Loot.wepList[b])
        else:
            pass


#Calls Loot drop roll
Loot.loot_drop_roll(Loot)


for x in Loot.drops:
    print(x.name)
    print(x.level)
    print(x.dmg)
Loot.loot_drop_roll(Loot)
for x in Loot.drops:
    print(x.name)
    print(x.level)
    print(x.dmg)