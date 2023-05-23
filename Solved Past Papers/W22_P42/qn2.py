# a)
class Character:
    def __init__(self, Name, XCoord, YCoord) -> None:
        self.__Name = Name # string
        self.__XCoordinate = XCoord # integer
        self.__YCoordinate = YCoord #integer

    # b)
    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    #c )
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate += int(XChange)
        self.__YCoordinate += int(YChange)

# d)
Game = [] # type Character Object

try:
    textFile = open("Characters.txt", 'r')
    for x in range(10):
        name = textFile.readline().strip()
        xCoord = textFile.readline().strip()
        yCoord = textFile.readline().strip()
        
        # create an object instance of class Character for above inputs from file
        characterObject = Character(name, int(xCoord), int(yCoord))

        # append character object to the Game array
        Game.append(characterObject)

except IOError:
    print("File can not be found")

# e)
name = ""
index = -1
while index == -1:
    raw_name = str(input("Enter character's name: "))
    name = raw_name.strip().lower()  # checking case -> Eg: Rohan == Rohan => True

    for x in range(10):
        if name == str(Game[x].GetName()).strip().lower(): # same case checking here too
            index = x # if found update the index variable
            break

validMoves = ["A", "W", "S", "D"]
direction = ""
while direction not in validMoves: # check if user input IS in validMoves array
    raw_direction = str(input("Enter the direction: "))
    direction = raw_direction.strip().upper()

    if direction == "A":
        Game[index].ChangePosition(-1, 0)
    elif direction == "W":
        Game[index].ChangePosition(0, 1)
    elif direction == "S":
        Game[index].ChangePosition(0, -1)
    elif direction == "D":
        Game[index].ChangePosition(1, 0) 

print(f"Qui has changed coordinates to X = {str(Game[index].GetX())} and Y = {str(Game[index].GetY())}")