class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [Node(1, 1), Node(5, 4), Node(6, 7), Node(7, -1), Node(2, 2),
                Node(0, 6), Node(0, 8), Node(56, 3), Node(0, 9), Node(0, -1)]

startPointer = 0
emptyList = 5

def outputNodes(linkedList, startPointer):
    nextPointer = startPointer
    while nextPointer != -1:
        print(f"Data: {linkedList[nextPointer].data} | Pointer: {nextPointer}")
        nextPointer = linkedList[nextPointer].nextNode

outputNodes(linkedList, startPointer)

def addNode(linkedList, currentPointer, emptyList):
    print("-------------------------------")
    data = int(input("Enter the data: "))

    if (emptyList < 0 and emptyList > 9):
        return False

    node = Node(data, -1)
    linkedList[emptyList] = node

    prevPointer = 0
    while (currentPointer != -1):
        prevPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode
    linkedList[prevPointer].nextNode = emptyList
    emptyList = linkedList[emptyList].nextNode

    return True

addNode(linkedList, 0, emptyList)
outputNodes(linkedList, startPointer)
