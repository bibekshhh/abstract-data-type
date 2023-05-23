global StackData, StackPointer

StackData = [0 for x in range(10)]
StackPointer = 0

def printData():
    global StackPointer, StackData
    for x in range(10):
        print(StackData[x])

    print(f"StackPointer: {StackPointer}")

printData()

def Push(item):
    global StackData, StackPointer
    if StackPointer == len(StackData):
        print("Stack is full")
        return False
    else:
        StackData[StackPointer] = item
        StackPointer += 1
        return True

def Pop():
    if StackPointer == 0:
        return -1
    else:
        data = StackData[StackPointer -1]
        StackPointer = StackPointer -1
        return data

Push(1)
Push(1)
Push(1)
Push(1)
Push(1)