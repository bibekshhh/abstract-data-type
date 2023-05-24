global Queue, HeadPointer, TailPointer

Queue = [-1 for x in range(100)]
HeadPointer = -1
TailPointer = 0

def Enqueue(newItem):
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        else:
            Queue[TailPointer] = newItem
            TailPointer += 1
            print("Successful")
            return True
    print("Unsuccessful")
    return False