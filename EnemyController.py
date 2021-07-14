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
    CR = 0

    enemy_pool = []


def spawn_enemy():

    enemy_types = ['Slime', 'Bat', 'Mole']
    a = random.randint(0, len(enemy_types)-1)

    lev = 1
    d = random.randint(1, 5)
    h = random.randint(1, 5)
    ed = (lev * d) * 2
    vs = (lev * h) * 2

    Enemy.e1 = Enemy(name=enemy_types[a],
               level=lev, CurrXP=0,
               MaxXP=100,
               hp=vs,
               enemy_dmg=ed,
               s_str=d,
               s_vit=h,
               )
    Enemy.e1.coins = random.randint(0, (10 * Enemy.e1.level))
    Enemy.e1.CR = d + h
    Enemy.enemy_pool = [Enemy.e1]


def print_stats():
    print('\n')

    def print_inventory():
        il = len(Enemy.enemy_pool[0].inventory)
        string_inventory = []
        for t in Enemy.enemy_pool[0].inventory[0:il]:
            b = t
            string_inventory.append(b.name)
        return string_inventory

    def print_equipped():
        el = list(Enemy.enemy_pool[0].equipped)
        el2 = []
        for pa in el:
            el2.append(pa.name)
        return el2

    player_info = {
                   'name': str(Enemy.enemy_pool[0].name),
                   'stats': ['Health: ' + str(Enemy.enemy_pool[0].hp),
                             "Attack: " + str(Enemy.enemy_pool[0].enemy_dmg),
                             "Strength " + str(Enemy.enemy_pool[0].s_str),
                             "Vitality " + str(Enemy.enemy_pool[0].s_vit)
                             ],
                   'level': Enemy.enemy_pool[0].level,
                   'Equipped': print_equipped(),
                   'Challenge Rating': Enemy.enemy_pool[0].CR,
                   'Items': print_inventory(),
                   'Coins': Enemy.enemy_pool[0].coins
                   }
    stats_list = ['Name:', 'Stats:', 'Level:', 'Equipped:', 'Challenge Rating']
    for (xa, a) in zip(stats_list, player_info.values()):
        print(str(xa) + ' ' + str(a))



