# Not completed ...

class Card:
    # Number as integer
    # Colour as string
    def __init__(self, number, colour):
        self.__number = number
        self.__colour = colour

    def GetNumber(self):
        return self.__number

    def GetColour(self):
        return self.__colour


# main
cardArray = [Card() for i in range(30)]

try:
    filename = "CardValues.txt"
    file = open(filename, "r")

    for i in range(30):
        numberVal = int(file.readline())
        colourVal = file.readline()

        cardArray[i] = Card(numberVal, colourVal)
    file.close()
except IOError:
    print("File not found.")
