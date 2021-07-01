#import needed classes
import QuestController
from PlayerController import Player
from LootController import Loot

global playerNameInput
global currQuest


def get_player_info():
    global playerNameInput
    playerNameInput = input("Enter your name\n")
    pass

#prints player's stats


def print_stats():
    player_info = {'name': [p1.name],
                   'stats':
                       ['Health:' + str(p1.hp),
                        "Attack: " + str(p1.player_dmg),
                        "Strength " + str(p1.s_str),
                        "Vitality " + str(p1.s_vit)
                        ],
                   'level': [p1.level],
                   'XP': [p1.pCurrXP, p1.pMaxXP],
                   'Quest': [p1.currQuest.name]}
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:']
    for (x, a) in zip(player_info.values(), stats_list):
        print(a, x)
    #print(
        #"Player Stats: " +
        #"\n Name: " + str(player_info.name) +
        #"\n  " + str(player_info.level) +
        #"\n  " + str(player_info.pCurrXP) + "/" + str(player_info.pMaxXP) +
        #"\n  " + str(player_info.hp) +
       # "\n  " + str(player_info.s_str) +
      #  "\n  " + str(player_info.s_vit) +
     #   "\n  " + str(player_info.player_dmg)
    #      )




def player_update():
    player_dmg_calc()

def rewards():
    Player.pCurrXP += 1
    if Player.pCurrXP >= Player.pMaxXP:
        print("congratulations "+Player.name + "\nYou are now level: " + Player.level)
    else:
        pass
    Loot.loot_drop(Loot)
    Inventory.coins += Loot.coinGain
    print(
                "Coins gained " + str(Loot.coinGain) + "\n" +
                "Coins Total " + str(Inventory.coins) + "\n")



#Equiped by player
class EquippedGear:
    class EquippedHelmet:
        def __init__(self):
            self.equip_type = "Helmet"
            self.name = ''
            self.level = ''
            self.pRes = 0
            self.mRes = 0



    class EquippedChest:

        equip_type = "Chest"
        name = ''
        level = ''
        pRes = 0
        mRes = 0

    class EquippedLegs:

        equip_type = "Legs"
        name = ''
        level = ''
        pRes = 0
        mRes = 0

    class EquippedWeapon:
        equip_type = "Weapon"
        name = ''
        level = ''
        dmg = 0


def player_dmg_calc():
    Player.player_dmg = round((EquippedGear.EquippedWeapon.dmg * p1.s_str)/2)


#Carried by player
class Inventory:
    coins = 0

    items_I = [Loot.wep1, Loot.a1, Loot.a2, Loot.a3]
    equipped_items = []
    equipping_item = []

    def select_item_equip(self):

        x = input("What item would you like to equip?\n")

        a = len(self.items_I)

        if int(x) > a or int(x) <= 0:
            print("Please enter a valid input between 0-" + str(a))
        else:
            b = self.items_I[int(x) - 1]
            if p1.level >= b.level:
                self.equipping_item.insert(1, b)
                self.items_I.remove(b)
                self.equip_item(self)
                self.equipping_item.remove(b)
            else:
                print("Your level is to low to equip this item.")



    #equips equipment
    def equip_item(self):

        for x in self.equipping_item:
            if x.equip_type == "Weapon":
                EquippedGear.EquippedWeapon.name = x.name
                EquippedGear.EquippedWeapon.level = x.level
                EquippedGear.EquippedWeapon.dmg = x.dmg
                try:
                    i = self.equipped_items[4]
                    self.items_I.append(i)
                except IndexError:
                    pass
                self.equipped_items.insert(4, x)
                print("Equipped Weapon!")
            elif x.equip_type == "Helmet":
                EquippedGear.EquippedWeapon.name = x.name
                EquippedGear.EquippedWeapon.level = x.level
                EquippedGear.EquippedWeapon.pRes = x.pRes
                EquippedGear.EquippedWeapon.mRes = x.mRes
                try:
                    i = self.equipped_items[1]
                    self.items_I.append(i)
                except IndexError:
                    pass
                self.equipped_items.insert(1, x)
                print("Equipped Helmet!")
            elif x.equip_type == "Chest":
                EquippedGear.EquippedWeapon.name = x.name
                EquippedGear.EquippedWeapon.level = x.level
                EquippedGear.EquippedWeapon.pRes = x.pRes
                EquippedGear.EquippedWeapon.mRes = x.mRes
                try:
                    i = self.equipped_items[2]
                    self.items_I.append(i)
                except IndexError:
                    pass
                self.equipped_items.insert(2, x)
                print("Equipped Chest!")
            elif x.equip_type == "Legs":
                EquippedGear.EquippedWeapon.name = x.name
                EquippedGear.EquippedWeapon.level = x.level
                EquippedGear.EquippedWeapon.pRes = x.pRes
                EquippedGear.EquippedWeapon.mRes = x.mRes
                try:
                    i = self.equipped_items[3]
                    self.items_I.append(i)
                except IndexError:
                    pass
                self.equipped_items.insert(3, x)
                print("Equipped Legs!")
            else:
                pass
            player_update()
    def show_equipped(self):

        for x in self.equipped_items:
            if x.equip_type == "Weapon":
                print(
                    "\n" +
                    str(x.name) + "\n" +
                    str(x.level) + "\n" +
                    str(x.dmg)
                    )
            else:
                print(
                    "\n" +
                    str(x.name) + "\n" +
                    str(x.level) + "\n" +
                    str(x.pRes) + "\n" +
                    str(x.mRes)
                    )


    def show_inventory(self):

        for x in self.items_I:
            print(x.name)

def quest_tracking():
    print(p1.currQuest)
    print(p1.qCurrObjective)
    print(p1.qCompObjective)
    # Current quest player is on
    currQuest = ''
    # Current Quest Objective
    qCurrObjective = ''
    # Completed Quest Objective
    qCompObjective = ''
def is_finished():

    if str(p1.qCurrObjective) == str(p1.qCompObjective):
        p1.qFinished = True
    else:
        p1.qFinished = False
#setup Player
get_player_info()
p1 = Player(name=str(playerNameInput),
            player_dmg=1,
            s_vit=1,
            s_str=1,
            level=1,
            pCurrXP=0,
            pMaxXP=100,
            hp=10,
            curr_quest=QuestController.q1,
            qCurrObjective=QuestController.q1.qCurrObjective,
            qCompObjective=QuestController.q1.qCompObjective
            )

#Test Inventory
Inventory.select_item_equip(Inventory)
Inventory.show_equipped(Inventory)
print("---------------------")
Inventory.show_inventory(Inventory)


#print("Player Health: " + str(Player.hp))
#print("Player Damage: " + str(Player.playerDmg))
#print("currency: " + str(Inventory.coins))

#print player stats
print_stats()
