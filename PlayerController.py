


class Player:
    def __init__(self):
        pass
    name = ''
    level = 1
    pCurrXP = 0
    pMaxXP = 100
    hp = 0
    playerDmg = 0
    s_str = 1
    s_vit = 1
    #Equiped by player
    class EquipedStats:
        class Helmet():
            def __init__(self, name, level, pRes, mRes):
                self.name = name
                self.level = level
                self.pRes = pRes
                self.mRes = mRes
        class Chest:
            def __init__(self, name, level, pRes, mRes):
                self.name = name
                self.level = level
                self.pRes = pRes
                self.mRes = mRes
        class Legs:
            def __init__(self, name, level, pRes, mRes):
                self.name = name
                self.level = level
                self.pRes = pRes
                self.mRes = mRes
        class Weapon:
            def __init__(self, name, level, dmg):
                self.name = name
                self.level = level
                self.dmg = dmg
    #Carried by player
    class Inventory:
        coins = 0
        items_I=[]
        #sets up equiped equipment
    def setup_epuiped(self):
        pass
        #setup to test system
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)

    #Calculates dmg for player
    def player_dmg_calc(self):
        self.playerDmg = (self.EquipedStats.Weapon.dmg + self.s_str)

    #prints player's stats
    def print_stats(self):
        print(
            "Player Stats: " +
            "\n Name: " + str(Player.name) +
            "\n Level: " + str(Player.level) +
            "\n XP : " + str(Player.pCurrXP) + "/" + str(Player.pMaxXP) +
            "\n Health: " + str(Player.hp) +
            "\n Strength: " + str(Player.s_str) +
            "\n Vitality: " + str(Player.s_vit)
              )
        pass
    #Equips the selected item
    def equip_item(self):
        pass
