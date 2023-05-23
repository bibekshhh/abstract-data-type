global playersList
playersList = [["", ""] for x in range(11)]

# print(playersList)

def ReadHighScores():
    try:
        textFile = open("HighScore.txt", 'r')
        # print(textFile.read())

        for x in range(10):
            playersList[x][0] = textFile.readline().strip("\n")
            playersList[x][1] = textFile.readline().strip("\n")

        print(playersList)
        textFile.close()
    except:
        print("Something went wrong")

ReadHighScores()


def OutputHighScores():
    for x in range(len(playersList)):
        print(f"{playersList[x][0]} {playersList[x][1]}")


def addPlayer(newPlayer, newScore):
    playersList[10][0] = newPlayer
    playersList[10][1] = newScore

    for x in range(len(playersList)):
        for y in range(len(playersList)-1):
            if int(playersList[y][1]) < int(playersList[y+1][1]):
                playersList[y][0], playersList[y+1][0] = playersList[y+1][0], playersList[y][0]
                playersList[y][1], playersList[y+1][1] = playersList[y+1][1], playersList[y][1]

def WriteTopTen():
    try:
        textFile = open("NewHighScore.txt", 'w')
        for x in range(len(playersList) -1):
            textFile.write(f"{str(playersList[x][0])}\n")
            textFile.write(f"{str(playersList[x][1])}\n")
        
        textFile.close()
    except:
        print("Something went wrong")


newPlayer = "ABCD"
newScore = -1

while len(newPlayer) != 3:
    newPlayer = str(input("Enter player's name: "))

while newScore < 1 or newScore > 100000:
    newScore = int(input("Enter new score: "))

addPlayer(newPlayer, newScore)
WriteTopTen()
# OutputHighScores()
print(playersList)