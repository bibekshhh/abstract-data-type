class TreeNode:
    def __init__(self):
        self.Data = ''
        self.LeftPointer = None
        self.RightPointer = None


RootPointer = 0
FreePointer = 0
size = 10


def Initialise():
    global TreeList, RootPointer, FreePointer

    RootPointer = None
    FreePointer = 0

    TreeList = [TreeNode() for i in range(size)]

    for i in range(size - 1):
        TreeList[i].LeftPointer = i + 1

    TreeList[size - 1].LeftPointer = None


def AddNode(item):
    global TreeList, RootPointer, FreePointer

    #if there is space
    
    if FreePointer is not None:

        #insert Node
        
        NewNodePointer = FreePointer
        FreePointer = TreeList[FreePointer].LeftPointer
        TreeList[NewNodePointer].Data = item
        TreeList[NewNodePointer].LeftPointer = None #it is the last node
        TreeList[NewNodePointer].RightPointer = None #so RP and LP should be Null

        #if first node
        
        if RootPointer == None:
            RootPointer = NewNodePointer

        #find insertion point
            
        else:
            ThisPointer = RootPointer
            PrevPointer = None

            while ThisPointer is not None:
                PrevPointer = ThisPointer

                if item < TreeList[ThisPointer].Data:
                    TurnedLeft = True
                    ThisPointer = TreeList[ThisPointer].LeftPointer
                else:
                    TurnedLeft = False
                    ThisPointer = TreeList[ThisPointer].RightPointer

            #jaa insert garyo tyasko pointer value change garne
                    
            if TurnedLeft:
                TreeList[PrevPointer].LeftPointer = NewNodePointer
            else:
                TreeList[PrevPointer].RightPointer = NewNodePointer


def Display():
    global TreeList, RootPointer, FreePointer

    for i in range(size):
        print(f"{i} || {TreeList[i].LeftPointer} || {TreeList[i].Data} || {TreeList[i].RightPointer}")


def FindNode(item):
    
    #start at the Root Pointer
    
    ThisPointer = RootPointer

    while ThisPointer is not None and TreeList[ThisPointer].Data != item:

        #check left or Right

        
        if item < TreeList[ThisPointer].Data:
            ThisPointer = TreeList[ThisPointer].LeftPointer
        else:
            ThisPointer = TreeList[ThisPointer].RightPointer

    return ThisPointer

def TraverseInOrder(TreeList, RootPointer):
    if TreeList[RootPointer].LeftPointer != None:
        TraverseInOrder(TreeList, TreeList[RootPointer].LeftPointer)
    print(str(TreeList[RootPointer].Data))
    if TreeList[RootPointer].RightPointer != None:
        TraverseInOrder(TreeList,TreeList[RootPointer].RightPointer)

            


    
Initialise()
Display()

AddNode('B')
AddNode('A')
AddNode('D')
AddNode('C')

print()

Display()

print()

print(FindNode('D'))

TraverseInOrder(TreeList, RootPointer)
