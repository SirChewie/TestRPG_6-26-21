#import needed classes
from PlayerController import Player
from LootController import Loot


def player_setup():
    Player.player_dmg_calc(Player)
    Player.hp = (10 * Player.s_vit)
    #Player.Inventory.items_I[0]

def rewards():
    Player.pCurrXP += 1
    if Player.pCurrXP >= Player.pMaxXP:
        print("Congradulations "+Player.name + "\nYou are now level: "+ Player.level)
    Player.Inventory.coins += 1

#setup Player
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
