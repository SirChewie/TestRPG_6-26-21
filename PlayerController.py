


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

    def setup_epuiped(self):
        pass
        #setup to test system
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)
        #Player.Inventory.items_I.append(Loot.TestWep.name)

    #Calculates dmg for player


    #prints player's stats
    def print_stats(self):
        print(
            "Player Stats: " +
            "\n Name: " + str(Player.name) +
            "\n Level: " + str(Player.level) +
            "\n XP : " + str(Player.pCurrXP) + "/" + str(Player.pMaxXP) +
            "\n Health: " + str(Player.hp) +
            "\n Strength: " + str(Player.s_str) +
            "\n Vitality: " + str(Player.s_vit) +
            "\n Attack: " + str(Player.playerDmg)
              )
        pass
    #Equips the selected item
