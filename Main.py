#import needed classes

from PlayerController import Player
from LootController import Loot

global playerNameInput

def get_player_info():
    global playerNameInput
    playerNameInput = input("Enter your name\n")
    pass

def player_setup():
    Player.player_dmg_calc(Player)
    Player.hp = (10 * Player.s_vit)
    Player.name = str(playerNameInput)
    pass

def rewards():
    Player.pCurrXP += 1
    if Player.pCurrXP >= Player.pMaxXP:
        print("congratulations "+Player.name + "\nYou are now level: " + Player.level)
    else:
        pass
    Player.Inventory.coins += 1
    pass



#setup Player
get_player_info()
player_setup()

#Test Inventory
print(Player.Inventory.items_I)
Player.setup_epuiped(Player)
print(Player.Inventory.items_I)

print("Player Health: " + str(Player.hp))
print("Player Damage: " + str(Player.playerDmg))
print("currency: " + str(Player.Inventory.coins))

#print player stats
Player.print_stats(Player)

