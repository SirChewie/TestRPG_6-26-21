


class Player:
    def __init__(self, name, level, pCurrXP, pMaxXP, hp, playerDmg, s_str, s_vit):
        self.name = name
        self.level = level
        self.pCurrXP = pCurrXP
        self.pMaxXP = pMaxXP
        self.hp = hp
        self.playerDmg = playerDmg
        self.s_str = s_str
        self.s_vit = s_vit
    #Equiped by player

    def setup_epuiped(self):
        pass
        #setup to test system
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)

    #Calculates dmg for player


