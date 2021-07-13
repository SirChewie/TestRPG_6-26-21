
global playerNameInput


class Player:

    def __init__(self,
                 name,
                 level,
                 CurrXP,
                 MaxXP,
                 hp,
                 player_dmg,
                 s_str,
                 s_vit):
        self.name = name
        self.level = level
        self.CurrXP = CurrXP
        self.MaxXP = MaxXP
        self.hp = hp
        self.player_dmg = player_dmg
        self.s_str = s_str
        self.s_vit = s_vit
    currQuest = ''
    qCurrObjective = ''
    qCompObjective = ''
    inventory = []
    equipped = []
    coins = 0
    dropMod = 1
    ran = False


def get_player_info():
    global playerNameInput
    playerNameInput = input("Enter your name\n")








