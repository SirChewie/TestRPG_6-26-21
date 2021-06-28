


class Player:
    def __init__(self):
        pass
    pCurrXP = 0
    pMaxXP = 100
    hp = 0
    playerDmg = 0
    s_str = 2
    s_vit = 10
    #Equiped by player
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
    #Carried by player
    class Inventory:
        coins = 0
        items_I=[]
        def setup_epuiped(self):
            Player.Inventory.items_I.append(Player.Test_Wep.name)
            Player.Inventory.items_I.append(Player.Test_Wep.level)
            Player.Inventory.items_I.append(Player.Test_Wep.dmg)

    def player_dmg_calc(self):
        self.playerDmg = (self.EquipedStats.Weapon.dmg + self.s_str)


