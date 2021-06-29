import random



class Loot:
    def __init__(self):
        pass

    ldr = []
    drops = []
    dropMod = 0

    class TestWep():
        equipType = 'Weapon'
        name = 'Axe'
        level = 1
        dmg = 5
    class TestWep2():
        equipType = 'Weapon'
        name = 'Sword'
        level = 2
        dmg = 7

    class TestArmor():
        equipType = 'Chest'
        name = 'Shirt'
        level = 1
        dmg = 2
    #Loot drop lists
    armorList = [TestArmor]
    wepList = [TestWep, TestWep2]
    lootList = [armorList, wepList]

    #What loot that was dropped?
    def loot_drop_roll(self):


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


    #Calls Loot drop roll x(numDrop) times
    def loot_drop(self):
        self.numDrops = 0

        self.numDrops = random.randint((1 + self.dropMod), (5 + self.dropMod))
        while self.numDrops > 0:
            Loot.loot_drop_roll(Loot)
            self.numDrops -= 1


    #prints out the item(s) info
        for x in Loot.drops:

            print(
                "\n" + str(x.equipType) + "\n" +
                str(x.name) + "\n" +
                str(x.level) + "\n" +
                str(x.dmg)
                )
        Loot.drops = []
Loot.loot_drop(Loot)