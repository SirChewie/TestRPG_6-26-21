#import needed classes
from PlayerController import Player
from LootController import Loot


def player_setup():
    Player.player_dmg_calc(Player)
    Player.hp = (10 * Player.s_vit)
    #Player.Inventory.items_I[0]

def rewards():
    Player.pCurrXP += 1
    Player.Inventory.coins += 1

#setup Player
player_setup()

#Test Inventory
print(Player.Inventory.items_I)
Player.Inventory.setup_epuiped(Player.Inventory)
print(Player.Inventory.items_I)

print("Player Health: " + str(Player.hp))
print("Player Damage: " + str(Player.playerDmg))
print("currency: " + str(Player.Inventory.coins))
print("Player Stats: \n Strength: " + str(Player.s_str) + "\n Vitality: " + str(Player.s_vit))
