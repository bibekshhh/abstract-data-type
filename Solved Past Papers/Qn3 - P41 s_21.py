class TreasureChest:
    def __init__(self, question, answer, points):
        self.__question = question  #question type string
        self.__answer = answer  #answer type integer
        self.__points = points  #points type integer

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, userAns):
        if userAns == self.__answer:
            return True
        return False

    def getPoints(self, numAttempts):
        if numAttempts == 1:
            return self.__points
        elif numAttempts == 2:
            return int(self.__points/2)
        elif numAttempts == 4:
            return int(self.__points/4)
        else:
            return 0

