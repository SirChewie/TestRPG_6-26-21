# import needed classes
import sys
import os

import EnemyController
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

    player_info = {'name': p1.name,
                   'stats':
                       ['Health: ' + str(p1.hp),
                        "Attack: " + str(p1.player_dmg),
                        "Strength " + str(p1.s_str),
                        "Vitality " + str(p1.s_vit)
                        ],
                   'level': p1.level,
                   'XP': str(p1.CurrXP) + "/" + str(p1.MaxXP),
                   'Quest': quest_tracking(),
                   'Equipped': print_equipped(),
                   'Items': print_inventory(),
                   'Coins': str(p1.coins)
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Quest:', 'Equipped:', 'Items:', 'Coins:']
    for (xa, a) in zip(player_info.values(), stats_list):
        print(a, xa)


def player_update():

    player_dmg_calc()


def rewards():
    p1.CurrXP += (10 * EnemyController.Enemy.enemy_pool[0].level)
    if p1.CurrXP >= p1.MaxXP:
        print("Congratulations " + str(p1.name) + "\nYou are now level: " + str(p1.level)+'!')
        p1.level += 1
        p1.CurrXP = (p1.CurrXP - p1.MaxXP)
        p1.MaxXP += (p1.MaxXP * .2)

    Loot.dropMod = p1.dropMod
    Loot.loot_drop(Loot)
    Loot.coinGain = EnemyController.Enemy.enemy_pool[0].coins
    for x in Loot.drops:
        p1.inventory.append(x)
    p1.coins += Loot.coinGain
    Loot.drops = []
    Loot.coinGain = 0


def player_dmg_calc():
    try:
        if p1.equipped[0].equip_type == 'Weapon':
            p1.player_dmg = p1.equipped[0].dmg * p1.s_str
        else:
            pass
    except IndexError:
        pass


def show_detailed_equipped():

    for x in p1.equipped:
        if x.equip_type == 'Weapon':
            print(
                "\n" +
                str(x.name) + "\n" +
                'Level: ' + str(x.level) + "\n" +
                'Damage: ' + str(x.dmg)
                )
        else:
            print(
                "\n" +
                str(x.name) + "\n" +
                'Level: ' + str(x.level) + "\n" +
                'Physical Resist: ' + str(x.pRes) + "\n" +
                'Magic Resist: ' + str(x.mRes)
                )


class InventoryManagement:
    equipping = []

    def select_item_equip(self):
        f = 1
        for ba in p1.inventory:
            print("\n" + str(f) + ": " + str(ba.name))
            f += 1
        if len(p1.inventory) < 1:
            print("No items to equip.")
        else:
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
                if p1.equipped[0].equip_type == 'Weapon':
                    req = p1.equipped[0]
                    p1.inventory.append(req)
                    p1.equipped.remove(req)
                    if req.name == 'No Weapon':
                        p1.inventory.remove(req)
                p1.equipped.insert(0, eq)
            elif x.equip_type == 'Helmet':
                eq = x
                try:
                    if p1.equipped[1].equip_type == 'Helmet':
                        req = p1.equipped[1]
                        p1.inventory.append(req)
                        p1.equipped.remove(req)
                        if req.name == 'No Helmet':
                            p1.inventory.remove(req)
                except IndexError:
                    print('IndexError')
                    pass
                p1.equipped.insert(1, eq)

            elif x.equip_type == 'Chest':
                eq = x
                try:
                    if p1.equipped[2].equip_type == 'Chest':
                        req = p1.equipped[2]
                        p1.inventory.append(req)
                        p1.equipped.remove(req)
                        if req.name == 'No Chest':
                            p1.inventory.remove(req)
                except IndexError:
                    print('IndexError')
                    pass
                p1.equipped.insert(2, eq)
            elif x.equip_type == 'Legs':
                eq = x
                try:
                    if p1.equipped[3].equip_type == 'Legs':
                        req = p1.equipped[3]
                        p1.inventory.append(req)
                        p1.equipped.remove(req)
                        if req.name == 'No Legs':
                            p1.inventory.remove(req)
                except IndexError:
                    print('IndexError')
                    pass
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
        # Continue
        elif x == '1':
            encounter()
        # Character
        elif x == '2':
            clear()
            print_stats()
            character_menu()
        # Shop
        elif x == '3':
            pass
        # Help
        elif x == '4':
            print("What would you like help with?")
        # Exit
        elif x == '5':
            sys.exit()
    except ValueError:
        print(Colors.fg.red+"Please enter a valid input(ValueError)"+Colors.reset)


def character_menu():
    menu = ['Equip an Item', 'Detailed Equipped Info', 'Help', 'Back']
    f = 1
    print('\nCHARACTER MENU' + "\n" + "---------------------")
    for xa in menu:
        print(str(f) + ": " + str(xa))
        f += 1
    x = str(input())
    lm = len(menu)
    try:
        if int(x) <= 0 or int(x) > lm:
            print(Colors.fg.red + "Please enter a valid input from 1-" + str(lm) + Colors.reset)
        # Equip an Item
        elif x == '1':
            InventoryManagement.select_item_equip(InventoryManagement)
        # Detailed Equipped Info
        elif x == '2':
            show_detailed_equipped()
        # Help
        elif x == '3':
            print("What would you like help with?")
        # Back
        elif x == '4':
            pass
    except ValueError:
        print(Colors.fg.red + "Please enter a valid input(ValueError)" + Colors.reset)


def combat_turn():

    menu = ['Attack', 'Use Item', 'Run']
    f = 1
    for xa in menu:
        print(str(f) + ": " + str(xa))
        f += 1
    x = str(input())
    lm = len(menu)
    try:
        if int(x) <= 0 or int(x) > lm:
            print(Colors.fg.red + "Please enter a valid input from 1-" + str(lm) + Colors.reset)
        # Attack
        elif x == '1':
            player_dmg_calc()
            print('\nYou hit ' + EnemyController.Enemy.enemy_pool[0].name +
                  ' for ' + str(p1.player_dmg) + ' damage!\n')
            EnemyController.Enemy.enemy_pool[0].hp -= p1.player_dmg

        # Use Item
        elif x == '2':
            pass
        # Back
        elif x == '3':
            print('You escaped!')
            EnemyController.Enemy.enemy_pool[0].hp = 0
            p1.ran = True
    except ValueError:
        print(Colors.fg.red + "Please enter a valid input(ValueError)" + Colors.reset)


def encounter():
    print('\nENCOUNTER!\n' + "---------------------")
    EnemyController.spawn_enemy()

    while EnemyController.Enemy.enemy_pool[0].hp > 0:
        clear()
        EnemyController.print_stats()
        combat_turn()
        if p1.ran is True:
            EnemyController.Enemy.enemy_pool[0].hp = 0
    if p1.ran is False:
        rewards()
    p1.ran = False

# setup Player
PC.get_player_info()

p1 = PC.Player(name=str(PC.playerNameInput),
               player_dmg=1,
               s_vit=1,
               s_str=1,
               level=1,
               CurrXP=0,
               MaxXP=100,
               hp=10
               )
p1.equipped = [Loot.wepSlot, Loot.armorSlotH, Loot.armorSlotC, Loot.armorSlotL]


# Keeps program running
try:
    while 1 < 2:
        main_menu()
except KeyboardInterrupt:
    sys.exit()
