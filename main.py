#import needed classes
import sys
import os
import QuestController
import PlayerController as PC
from LootController import Loot
from TextColorContoller import Colors


global playerNameInput
global currQuest


def clear():
    os.system('cls')


    def print_stats():

        def print_inventory():
            il = len(PC.p1.inventory)
            string_inventory = []
            for t in PC.p1.inventory[0:il]:
                b = t
                string_inventory.append(b.name)
            return string_inventory

        def print_equipped():
            el = list(PC.p1.equipped)
            el2 = []
            for pa in el:
                el2.append(pa.name)
            return el2

        player_info = {'name': [PC.p1.name],
                       'stats':
                           ['Health: ' + str(PC.p1.hp),
                            "Attack: " + str(PC.p1.player_dmg),
                            "Strength " + str(PC.p1.s_str),
                            "Vitality " + str(PC.p1.s_vit)
                            ],
                       'level': [PC.p1.level],
                       'XP': [PC.p1.pCurrXP, PC.p1.pMaxXP],
                       'Quest': quest_tracking(),
                       'Equipped': print_equipped(),
                       'Items': print_inventory(),
                       'Coins': [PC.p1.coins]
                       }
        stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:', 'Equipped:', 'Items:']
        for (xa, a) in zip(player_info.values(), stats_list):
            print(a, xa)

def player_update():

    player_dmg_calc()


def rewards():
    PC.p1.pCurrXP += 1
    if PC.p1.pCurrXP >= PC.p1.pMaxXP:
        print("congratulations " + PC.p1.name + "\nYou are now level: " + PC.p1.level)
    else:
        pass
    Loot.loot_drop(Loot)


def player_dmg_calc():
    if PC.p1.equipped[0].equip_type == 'Weapon':
        PC.p1.player_dmg = round((PC.p1.equipped[0].dmg * PC.p1.s_str))
    else:
        pass


def show_detailed_equipped():

    for x in PC.p1.equipped:
        if x.equip_type == 'Weapon':
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

# prints player's stats
def print_stats():

    def print_inventory():
        il = len(PC.p1.inventory)
        string_inventory = []
        for t in PC.p1.inventory[0:il]:
            b = t
            string_inventory.append(b.name)
        return string_inventory

    def print_equipped():
        el = list(PC.p1.equipped)
        el2 = []
        for pa in el:
            el2.append(pa.name)
        return el2

    player_info = {'name': [PC.p1.name],
                   'stats':
                       ['Health: ' + str(PC.p1.hp),
                        "Attack: " + str(PC.p1.player_dmg),
                        "Strength " + str(PC.p1.s_str),
                        "Vitality " + str(PC.p1.s_vit)
                        ],
                   'level': [PC.p1.level],
                   'XP': [PC.p1.pCurrXP, PC.p1.pMaxXP],
                   'Quest': quest_tracking(),
                   'Equipped': print_equipped(),
                   'Items': print_inventory(),
                   'Coins': [PC.p1.coins]
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:', 'Equipped:', 'Items:']
    for (xa, a) in zip(player_info.values(), stats_list):
        print(a, xa)
class InventoryManagement:
    equipping = []

    def select_item_equip(self):
        f = 1
        for ba in PC.p1.inventory:
            print("\n" + str(f) + ": " + str(ba.name))
            f += 1
        try:
            x = int(input("What item would you like to equip?\n"))
            a = len(PC.p1.inventory)

            if int(x) > a or int(x) <= 0:
                print("Please enter a valid input between 0-" + str(a))
                self.select_item_equip(self)
            else:
                b = PC.p1.inventory[int(x) - 1]
                if PC.p1.level >= b.level:
                    self.equipping.insert(1, b)
                    PC.p1.inventory.remove(b)
                    self.equip_item(self)
                    self.equipping.remove(b)
                else:
                    print("Your level is to low to equip this item.")
                    self.select_item_equip(self)
        except ValueError:
            print("Please enter an integer only.")
            self.select_item_equip(self)
        self.equipping = []

    # equips equipment
    def equip_item(self):

        for x in self.equipping:
            if x.equip_type == 'Weapon':
                eq = x
                PC.p1.equipped.insert(0, eq)
            elif x.equip_type == 'Helmet':
                eq = x
                PC.p1.equipped.insert(1, eq)
            elif x.equip_type == 'Chest':
                eq = x
                PC.p1.equipped.insert(2, eq)
            elif x.equip_type == 'Legs':
                eq = x
                PC.p1.equipped.insert(3, eq)

        player_update()


def quest_tracking():
    # Current quest player is on
    PC.p1.currQuest = QuestController.q1.name
    # Current Quest Objective
    PC.p1.qCurrObjective = QuestController.q1.qCurrObjective
    # Completed Quest Objective
    PC.p1.qCompObjective = QuestController.q1.qCompObjective


def is_finished():

    if str(PC.p1.qCurrObjective) == str(PC.p1.qCompObjective):
        QuestController.q1.qFinished = True
    else:
        pass


def main_menu():
    menu = ['Continue', 'Character', 'Shop', 'Help', 'Exit']
    f = 1
    print('\nMAIN MENU' + "\n" + "---------------------")
    for xa in menu:
        print(str(f) + ": " + str(xa))
        f += 1
    x = str(input())
    lm = len(menu)
    try:
        if int(x) <= 0 or int(x) > lm:
            print(Colors.fg.red+"Please enter a valid input from 1-"+str(lm)+Colors.reset)
        elif x == '1':
            pass
        elif x == '2':
            clear()
            print_stats()
            InventoryManagement.select_item_equip(InventoryManagement)
        elif x == '3':
            pass
        elif x == '4':
            print("What would you like help with?")
        elif x == '5':
            sys.exit()
    except ValueError:
        print(Colors.fg.red+"Please enter a valid input(ValueError)"+Colors.reset)


# setup Player
PC.get_player_info()

p1 = PC.Player(name=str(PC.playerNameInput),
               player_dmg=1,
               s_vit=1,
               s_str=1,
               level=1,
               pCurrXP=0,
               pMaxXP=100,
               hp=10
               )

#print player stats
print_stats()


#Keeps program running
try:
    while 1 < 2:
        main_menu()
except KeyboardInterrupt:
    sys.exit()
