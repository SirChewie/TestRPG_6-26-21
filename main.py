# import needed classes
import sys
import os

import EnemyController
import LootController
import QuestController
import PlayerController as PC
import ShopSystem
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
                        "Vitality " + str(p1.s_vit),
                        'Physical Resist ' + str(p1.pRes),
                        'Magic Resist ' + str(p1.mRes)
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
    player_def_calc()
    ShopSystem.player_coins = p1.coins


def rewards():
    clear()
    p1.CurrXP += (10 * EnemyController.Enemy.enemy_pool[0].level)
    if p1.CurrXP >= p1.MaxXP:
        p1.level += 1
        print("Congratulations " + str(p1.name) + "\nYou are now level: " + str(p1.level)+'!')
        p1.CurrXP = (p1.CurrXP - p1.MaxXP)
        p1.MaxXP += (p1.MaxXP * .2)
        EnemyController.plvl += 1

    Loot.dropMod = p1.dropMod
    Loot.loot_drop(Loot)
    Loot.coinGain = EnemyController.Enemy.enemy_pool[0].coins
    for x in Loot.drops:
        p1.inventory.append(x)
    p1.coins += Loot.coin_total
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


def player_def_calc():
    pr = 0
    mr = 0
    try:
        for x in p1.equipped:
            if x.equip_type == 'Helmet':
                pr += x.pRes
                mr += x.mRes
            elif x.equip_type == 'Chest':
                pr += x.pRes
                mr += x.mRes
            elif x.equip_type == 'Legs':
                pr += x.pRes
                mr += x.mRes
            else:
                pass
    except IndexError:
        pass
    p1.pRes = (pr + 1)
    p1.mRes = (mr + 1)


def show_detailed_equipped():
    print('\nEquipped Gear' + "\n" + "---------------------")
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
    clear()
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
            character_menu()
        # Shop
        elif x == '3':
            clear()
            ShopSystem.player_coins = p1.coins
            shop_menu()
        # Help
        elif x == '4':
            clear()
            print("What would you like help with?")
        # Exit
        elif x == '5':
            print("Good bye")
            sys.exit()
    except ValueError:
        print(Colors.fg.red+"Please enter a valid input(ValueError)"+Colors.reset)


def character_menu():
    clear()

    menu = ['Equip an Item', 'Detailed Equipped Info', 'Help', 'Back']
    f = 1
    print('\nCHARACTER MENU' + "\n" + "---------------------")
    print_stats()
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
            input('\nPress Enter to continue.')
        # Help
        elif x == '3':
            print("What would you like help with?")
        # Back
        elif x == '4':
            pass
    except ValueError:
        print(Colors.fg.red + "Please enter a valid input(ValueError)" + Colors.reset)


def shop_menu():

    print('You have ' + str(p1.coins) + ' coins')
    menu = ['Buy', 'Sell', 'Help', 'Back']
    f = 1
    print('\nSHOP' + "\n" + "---------------------")
    for xa in menu:
        print(str(f) + ": " + str(xa))
        f += 1
    x = str(input())
    try:
        if x == '1':
            print('What would you like to buy?')
            for sx in ShopSystem.shopSell:
                get_values()
                print(sx.value)
        elif x == '2':
            selling = []
            get_values()
            s = 1
            for x in p1.inventory:
                print(str(s) + ': ' + str(x.name) + ', value: ' + str(x.value))
                s += 1

            def selling_items():
                try:
                    eq = input('What would you like to sell?\n')
                    xs = p1.inventory[(int(eq)-1)]
                    selling.append(xs)
                    p1.inventory.remove(xs)
                    print('1: Yes\n2: No')
                    e = input('Would you like to sell anything else?')
                    if e == '1':
                        selling_items()
                    else:
                        pass
                    for a in selling:
                        p1.coins += a.value
                        selling.remove(a)
                except ValueError:
                    print("Please enter an integer only.")
                    shop_menu()
            selling_items()

        elif x == '3':
            print('What would you like help with?')
        elif x == '4':
            pass
    except ValueError:
        print("Please enter a valid input(ValueError)")


def get_values():
    for x in p1.inventory:
        if x.equip_type == 'Weapon':
            x.value = (x.level * x.dmg)
        else:
            x.value = (x.level * (x.pRes + x.mRes))


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
            clear()
            player_update()
            print('\nYou hit ' + EnemyController.Enemy.enemy_pool[0].name +
                  ' for ' + str(p1.player_dmg) + ' damage!\n')
            EnemyController.Enemy.enemy_pool[0].hp -= p1.player_dmg

        # Use Item
        elif x == '2':
            pass
        # Back
        elif x == '3':
            clear()
            EnemyController.Enemy.enemy_pool[0].hp = 0
            p1.ran = True
    except ValueError:
        print(Colors.fg.red + "Please enter a valid input(ValueError)" + Colors.reset)
        combat_turn()


def enemy_turn():
    try:
        epdc = EnemyController.Enemy.enemy_pool[0].enemy_dmg / p1.pRes
        emdc = EnemyController.Enemy.enemy_pool[0].enemy_dmg / p1.mRes
    except ZeroDivisionError:
        epdc = 1
        emdc = 1
    x = int(EnemyController.Enemy.enemy_pool[0].enemy_dmg/epdc)
    m = int(EnemyController.Enemy.enemy_pool[0].enemy_dmg/emdc)
    p1.currHP -= x
    print('You received ' + str(x) + ' damage')


def encounter():
    maxpHP = p1.hp
    p1.currHP = p1.hp
    print('\nENCOUNTER!\n' + "---------------------")
    EnemyController.spawn_enemy()
    clear()
    while EnemyController.Enemy.enemy_pool[0].hp > 0:
        EnemyController.print_stats()
        print(p1.currHP)
        combat_turn()
        if p1.ran is True:
            EnemyController.Enemy.enemy_pool[0].hp = 0
            input('You got away! \n Press Enter to continue.')
            p1.hp = maxpHP
            break
        elif EnemyController.Enemy.enemy_pool[0].hp <= 0:
            break
        EnemyController.print_stats()
        print(p1.currHP)
        enemy_turn()
        if p1.currHP <= 0:
            p1.ran = True
            clear()
            EnemyController.Enemy.enemy_pool[0].hp = 0
            input('You died... \n Press Enter to continue.')
            p1.hp = maxpHP
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
