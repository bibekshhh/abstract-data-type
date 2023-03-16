#Qno: 2
class Balloon:
    #Health as integer
    #Colour as string
    #DefenceItem as string
    def __init__(self, colour, DefenceItem):
        self.__health = 100
        self.__colour = colour
        self.__DefenceItem = DefenceItem

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, newHealth):
        self.__health = self.__health + newHealth

    def CheckHealth(self):
        if (self.__health <= 0):
            return True
        return False
    

colour = input("Enter the colour: ")
DefenceItem = input("Enter the defence item: ")

Balloon1 = Balloon(colour, DefenceItem)

def defend(Balloon1):
    opponentStrength = int(input("Enter the opponent's strength: "))

    Balloon1.ChangeHealth(-opponentStrength)

    print(Balloon1.GetDefenceItem())

    if (Balloon1.CheckHealth() == True):
        print("Defence succeeded")
    print("Defence failed")

    return Balloon1

Balloon1 = defend(Balloon1)



















