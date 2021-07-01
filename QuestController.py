class Quests():
    def __init__(self, name, levelReq, xpGain,qCurrObjective,qCompObjective, qFinished):
        self.name = name
        self.levelReq = levelReq
        self.xpGain = xpGain
        self.qCurrObjective = qCurrObjective
        self.qCompObjective = qCompObjective
        self.qFinished = qFinished

    def quest_updater(self):
        pass

finishedQuests = []


q1 = Quests(name='Introduction',
            levelReq=0,
            xpGain=10,
            qCurrObjective="Learning to play",
            qCompObjective=None,
            qFinished=False
            )

quest_dict = [q1]
