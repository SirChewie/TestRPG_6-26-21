import random

import EnemyController


class Loot:
    def __init__(self):
        pass

    ldr = []
    drops = []
    dropMod = 0
    coinGain = 0

    class Wep:
        def __init__(self, equip_type, name, level, dmg):
            self.equip_type = equip_type
            self.name = name
            self.level = level
            self.dmg = dmg
        value = 0

    wep1 = Wep('Weapon', 'Axe', 1, 2)
    wepList = [wep1]
    wepSlot = Wep('Weapon', 'No Weapon', 1, 1)

    class Armor:
        def __init__(self, equip_type, name, level, pRes, mRes):

            self.equip_type = equip_type
            self.name = name
            self.level = level
            self.pRes = pRes
            self.mRes = mRes
        value = 0
    a1 = Armor('Helmet', 'Cloth Hat', 1, 1, 0)
    a2 = Armor('Chest', 'Cloth Shirt', 1, 1, 0)
    a3 = Armor('Legs', 'Cloth Pants', 1, 1, 0)
    armorSlotH = Armor('Helmet', 'No Helmet', 0, 0, 0)
    armorSlotC = Armor('Chest', 'No Chest', 0, 0, 0)
    armorSlotL = Armor('Legs', 'No Legs', 0, 0, 0)
    armorList = [a1, a2, a3]
    # Loot drop lists
    noneList = []
    lootList = [armorList, wepList, noneList]



    # What loot that was dropped?
    def loot_drop_roll(self):

        i = random.randint(0, (len(Loot.lootList) - 1))
        self.coinGain = random.randint(1, 10)
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

    # Calls Loot drop roll x(numDrop) times
    def loot_drop(self):
        self.numDrops = 0

        self.numDrops = random.randint((1 * self.dropMod), (2 * self.dropMod))
        while self.numDrops > 0:
            Loot.loot_drop_roll(Loot)
            self.numDrops -= 1
        print('THE MONSTER WAS CARRYING SOMETHING!')
        print('Coins: ' + str(Loot.coinGain))
    # prints out the item(s) info
        for x in Loot.drops:
            if x.equip_type == 'Weapon':
                print(
                    "\nEquipment type: " + str(x.equip_type) + "\n" +
                    str(x.name) + "\n" +
                    "Level req: " + str(x.level) + "\n" +
                    "Attack: " + str(x.dmg) + "\n"
                    )
            else:
                print(
                    "\nEquipment type: " + str(x.equip_type) + "\n" +
                    str(x.name) + "\n" +
                    "Level req: " + str(x.level) + "\n" +
                    "Physical Res: " + str(x.pRes) + "\n" +
                    "Magic Res: " + str(x.mRes) + "\n"
                    )

        input("Press Enter to continue")
