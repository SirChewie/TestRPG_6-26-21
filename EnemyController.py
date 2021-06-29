import LootController

class Enemy:
    def __init__(self):
        pass
    name = ''
    level = 1
    pCurrXP = 0
    pMaxXP = 100
    hp = 0
    playerDmg = 0
    s_str = 2
    s_vit = 10
    #Equiped by Enemy
    class EquipedStats:
        class Helmet:
            name = ''
            level = 0
            pRes = 0
            mRes = 0
        class Armor:
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
    #Carried by Enemy
    class Inventory:
        coins = 0
        items_I=[]
        #sets up equiped equipment
    def setup_epuiped(self):
        #setup to test system
        Enemy.Inventory.items_I.append(LootController.Loot.TestWep.name)
        Enemy.Inventory.items_I.append(LootController.Loot.TestWep.name)
        Enemy.Inventory.items_I.append(LootController.Loot.TestWep.name)

    #Calculates dmg for Enemy
    def player_dmg_calc(self):
        self.playerDmg = (self.EquipedStats.Weapon.dmg + self.s_str)

    #prints Enemy's stats
    def print_stats(self):
        print(
            "Player Stats: " +
            "\n Name: " + str(Enemy.name) +
            "\n Level: " + str(Enemy.level) +
            "\n XP : " + str(Enemy.pCurrXP) + "/" + str(Enemy.pMaxXP) +
            "\n Health: " + str(Enemy.hp) +
            "\n Strength: " + str(Enemy.s_str) +
            "\n Vitality: " + str(Enemy.s_vit)
              )