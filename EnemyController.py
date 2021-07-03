import random


class Enemy:

    def __init__(self,
                 name,
                 level,
                 CurrXP,
                 MaxXP,
                 hp,
                 enemy_dmg,
                 s_str,
                 s_vit):
        self.name = name
        self.level = level
        self.CurrXP = CurrXP
        self.MaxXP = MaxXP
        self.hp = hp
        self.enemy_dmg = enemy_dmg
        self.s_str = s_str
        self.s_vit = s_vit
    inventory = []
    equipped = []
    coins = 0


    enemy_pool = []


def spawn_enemy():

    enemy_types = ['Slime', 'Bat', 'Mole']
    a = random.randint(0, len(enemy_types)-1)

    lev = 1
    d = random.randint(1, 5)
    h = random.randint(1, 5)
    ed = (lev * d) * 10
    vs = (lev * h) * 10

    Enemy.e1 = Enemy(name=enemy_types[a],
               level=lev, CurrXP=0,
               MaxXP=100,
               hp=vs,
               enemy_dmg=ed,
               s_str=d,
               s_vit=h,
               )
    Enemy.enemy_pool = [Enemy.e1]


def print_stats():

    def print_inventory():
        il = len(Enemy.e1.inventory)
        string_inventory = []
        for t in Enemy.e1.inventory[0:il]:
            b = t
            string_inventory.append(b.name)
        return string_inventory

    def print_equipped():
        el = list(Enemy.e1.equipped)
        el2 = []
        for pa in el:
            el2.append(pa.name)
        return el2

    player_info = {'name': [Enemy.e1.name],
                   'stats':
                       ['Health: ' + str(Enemy.e1.hp),
                        "Attack: " + str(Enemy.e1.enemy_dmg),
                        "Strength " + str(Enemy.e1.s_str),
                        "Vitality " + str(Enemy.e1.s_vit)
                        ],
                   'level': [Enemy.e1.level],
                   'XP': [Enemy.e1.CurrXP, Enemy.e1.MaxXP],
                   'Equipped': print_equipped(),
                   'Items': print_inventory(),
                   'Coins': [Enemy.e1.coins]
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'XP:', 'Equipped:', 'Items:']
    for (xa, a) in zip(player_info.values(), stats_list):
        print(a, xa)