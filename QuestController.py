class Quests():
    def __init__(self):
        pass

    #Current quest player is on
    currQuest = ''
    #Current Quest Objective
    qCurrObjective = ''
    #Completed Quest Objective
    qCompObjective = ''

    finishedQuests = []
    class introduction():
        name = 'Introduction'
        levelReq = 0
        xpGain = 10
        qFinished = False

def is_finished(self):
    if (str(self.qCurrObjective) == str(self.qCompObjective)):
        self.qFinished = True
    else:
        self.qFinished = False
