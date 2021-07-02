
class Player:

    def __init__(self,
                 name,
                 level,
                 pCurrXP,
                 pMaxXP,
                 hp,
                 player_dmg,
                 s_str,
                 s_vit):
        self.name = name
        self.level = level
        self.pCurrXP = pCurrXP
        self.pMaxXP = pMaxXP
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

    #Equipped by player




