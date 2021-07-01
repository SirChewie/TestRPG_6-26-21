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

    def print_inventory():
        l = len(p1.inventory)
        string_inventory = []
        for t in p1.inventory[0:l]:
            b = t
            string_inventory.append(b.name)
        return string_inventory

    def print_equipped():
        el = list(p1.equipped.values())
        el2 = []
        for a in el:
            el2.append(a.name)
        return el2



    player_info = {'name': [p1.name],
                   'stats':
                       ['Health: ' + str(p1.hp),
                        "Attack: " + str(p1.player_dmg),
                        "Strength " + str(p1.s_str),
                        "Vitality " + str(p1.s_vit)
                        ],
                   'level': [p1.level],
                   'XP': [p1.pCurrXP, p1.pMaxXP],
                   'Quest': [None],
                   'Equipped': [print_equipped()],
                   'Items': [print_inventory()],
                   'Coins': [p1.coins]
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:', 'Equipped:', 'Items:']
    for (xa, a) in zip(player_info.values(), stats_list):
        print(a, xa)





def player_update():
    player_dmg_calc()

def rewards():
    Player.pCurrXP += 1
    if Player.pCurrXP >= Player.pMaxXP:
        print("congratulations "+Player.name + "\nYou are now level: " + Player.level)
    else:
        pass
    Loot.loot_drop(Loot)








def player_dmg_calc():
    p1.player_dmg = round((p1.equipped['Weapon'].dmg * p1.s_str)/2)


class InventoryManagement:

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

        # equips equipment
        def equip_item(self):

            for x in self.equipping_item:
                if x.equip_type == "Weapon":
                    name = x.name
                    level = x.level
                    dmg = x.dmg
                    try:
                        i = self.equipped_items[4]
                        self.items_I.append(i)
                    except IndexError:
                        pass
                    self.equipped_items.insert(4, x)
                    print("Equipped Weapon!")
                elif x.equip_type == "Helmet":
                    name = x.name
                    level = x.level
                    pRes = x.pRes
                    mRes = x.mRes
                    try:
                        i = self.equipped_items[1]
                        self.items_I.append(i)
                    except IndexError:
                        pass
                    self.equipped_items.insert(1, x)
                    print("Equipped Helmet!")
                elif x.equip_type == "Chest":
                    name = x.name
                    level = x.level
                    pRes = x.pRes
                    mRes = x.mRes
                    try:
                        i = self.equipped_items[2]
                        self.items_I.append(i)
                    except IndexError:
                        pass
                    self.equipped_items.insert(2, x)
                    print("Equipped Chest!")
                elif x.equip_type == "Legs":
                    name = x.name
                    level = x.level
                    pRes = x.pRes
                    mRes = x.mRes
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
#Equipped by player

p1 = Player(name=str(playerNameInput),
            player_dmg=1,
            s_vit=1,
            s_str=1,
            level=1,
            pCurrXP=0,
            pMaxXP=100,
            hp=10
            )
equipping = [Loot.wep1, Loot.a1, Loot.a2, Loot.a3]
for x in equipping:
    eq = x
    p1.equipped.update({str(eq.equip_type): eq})

#Test Inventory
print("---------------------")

#print player stats
print_stats()
