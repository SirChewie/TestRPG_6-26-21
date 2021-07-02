#import needed classes
import sys

import QuestController
from PlayerController import Player
from LootController import Loot

global playerNameInput
global currQuest


def get_player_info():
    global playerNameInput
    playerNameInput = input("Enter your name\n")

#prints player's stats


def print_stats():

    def print_inventory():
        il = len(p1.inventory)
        string_inventory = []
        for t in p1.inventory[0:il]:
            b = t
            string_inventory.append(b.name)
        return string_inventory

    def print_equipped():
        el = list(p1.equipped)
        el2 = []
        for pa in el:
            el2.append(pa.name)
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
                   'Quest': quest_tracking(),
                   'Equipped': print_equipped(),
                   'Items': print_inventory(),
                   'Coins': [p1.coins]
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:', 'Equipped:', 'Items:']
    for (xa, a) in zip(player_info.values(), stats_list):
        print(a, xa)


def player_update():

    player_dmg_calc()

def rewards():
    p1.pCurrXP += 1
    if p1.pCurrXP >= p1.pMaxXP:
        print("congratulations " + p1.name + "\nYou are now level: " + p1.level)
    else:
        pass
    Loot.loot_drop(Loot)


def player_dmg_calc():
    if p1.equipped[0].equip_type == 'Weapon':
        p1.player_dmg = round((p1.equipped[0].dmg * p1.s_str))
    else:
        pass


def show_detailed_equipped():

    for x in p1.equipped:
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


class InventoryManagement:
    equipping = []

    def select_item_equip(self):
        f = 1
        for ba in p1.inventory:
            print("\n" + str(f) + ": " + str(ba.name))
            f += 1
        try:
            x = int(input("What item would you like to equip?\n"))
            a = len(p1.inventory)

            if int(x) > a or int(x) <= 0:
                print("Please enter a valid input between 0-" + str(a))
                self.select_item_equip(self)
            else:
                b = p1.inventory[int(x) - 1]
                if p1.level >= b.level:
                    self.equipping.insert(1, b)
                    p1.inventory.remove(b)
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
                p1.equipped.insert(0, eq)
            elif x.equip_type == 'Helmet':
                eq = x
                p1.equipped.insert(1, eq)
            elif x.equip_type == 'Chest':
                eq = x
                p1.equipped.insert(2, eq)
            elif x.equip_type == 'Legs':
                eq = x
                p1.equipped.insert(3, eq)

        player_update()


def quest_tracking():
    # Current quest player is on
    p1.currQuest = QuestController.q1.name
    # Current Quest Objective
    p1.qCurrObjective = QuestController.q1.qCurrObjective
    # Completed Quest Objective
    p1.qCompObjective = QuestController.q1.qCompObjective


def is_finished():

    if str(p1.qCurrObjective) == str(p1.qCompObjective):
        QuestController.q1.qFinished = True
    else:
        pass


#setup Player
get_player_info()
p1 = Player(name=str(playerNameInput),
            player_dmg=1,
            s_vit=1,
            s_str=1,
            level=1,
            pCurrXP=0,
            pMaxXP=100,
            hp=10
            )

#Test Inventory
print("---------------------")

#print player stats
print_stats()

try:
    while 1 < 2:
        InventoryManagement.select_item_equip(InventoryManagement)
except KeyboardInterrupt:
    sys.exit()
