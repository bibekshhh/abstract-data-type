class Node: 
    def __init__(self) -> None:
        self.leftPtr = None
        self.rightPtr = None
        self.data = ""

class BinaryTree:
    def __init__(self) -> None:
        self.rootPtr = 0
        self.freePtr = 0
        self.TreeList = [Node() for x in range(5)]
        self.length = len(self.TreeList)

    def Initialise(self):
        self.rootPtr = None
        self.freePtr = 0

        for x in range(self.length -1):
            self.TreeList[x].leftPtr = x +1
            
        self.TreeList[self.length -1].leftPtr = None

    def Display(self):
        for x in range(self.length):
            print(f"Index: {x} | LeftPtr: {self.TreeList[x].leftPtr} | Data: {self.TreeList[x].data} | RightPtr: {self.TreeList[x].rightPtr}")


    def AddNode(self, newItem):
        # check if space available for new node
        if (self.freePtr is not None):
            # add new node 
            newNodePtr = self.freePtr
            self.freePtr = self.TreeList[self.freePtr].leftPtr
            self.TreeList[newNodePtr].leftPtr = None
            self.TreeList[newNodePtr].right = None
            self.TreeList[newNodePtr].data = newItem

            # check if first node empty
            if (self.rootPtr is None):
                # if empty link the added node to the rootPtr:
                self.rootPtr = newNodePtr
            
            # else find insertion point
            else: 
                thisPtr = self.rootPtr
                prevPtr = None

                while thisPtr is not None:
                    prevPtr = thisPtr

                    if newItem < self.TreeList[thisPtr].data:
                        turnedLeft = True
                        thisPtr = self.TreeList[thisPtr].leftPtr
                    else: 
                        turnedLeft = False
                        thisPtr = self.TreeList[thisPtr].rightPtr

                if turnedLeft: # if true
                    self.TreeList[prevPtr].leftPtr = newNodePtr           
                else:
                    self.TreeList[prevPtr].rightPtr = newNodePtr     

    def FindNode(self, item):
        thisPtr = self.rootPtr 

        while thisPtr is not None and self.TreeList[thisPtr].data != item:
            if (item < self.TreeList[thisPtr].data):
                thisPtr = self.TreeList[thisPtr].leftPtr
            else:
                thisPtr = self.TreeList[thisPtr].rightPtr

        print("")
        print("======= Found Node =======")
        print(f"\nNode found at index: {thisPtr}")
        return thisPtr


    def Traversal(self, TreeList, RootPtr):
        if (self.TreeList[RootPtr].leftPtr != None):
            self.Traversal(TreeList, self.TreeList[RootPtr].leftPtr)
        print(str(self.TreeList[RootPtr].data), "-> ", end="")

        if (self.TreeList[RootPtr].rightPtr != None):
            self.Traversal(TreeList, self.TreeList[RootPtr].rightPtr)


Tree = BinaryTree()
Tree.Initialise()

# Tree.Display()

Tree.AddNode("B")
Tree.AddNode("A")
Tree.AddNode("D")
Tree.AddNode("C")

# Display tree after node added
print("")
print("============ Tree after node added ============")
print("")

Tree.Display()

# Display tree after traversal
print("")
print("============ Tree after traversal ============")
print("")

Tree.Traversal(Tree.TreeList, Tree.rootPtr)

Tree.FindNode("C")