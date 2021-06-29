


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
        class Helmet:
            name = ''
            level = 0
            pRes = 0
            mRes = 0
        class Chest:
            name = ''
            level = 0
            pRes = 0
            mRes = 0
        class Legs:
            name = ''
            level = 0
            pRes = 0
            mRes = 0
        class Weapon:
            name = ''
            level = 0
            dmg = 1
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
